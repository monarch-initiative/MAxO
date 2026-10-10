#!/usr/bin/env python3
"""Translate the MAxO source (as Turtle) into YAML validatable with linkml-validate.

The translation is driven by the LinkML schema (src/schema/maxo_schema.yaml):
each schema slot_uri decides which YAML key an annotation lands in. Nothing is
judged here - properties the schema does not know are emitted under their CURIE
and the (closed) schema rejects them. See the schema description for the value
encoding.

Usage:
    maxo_to_linkml.py --schema maxo_schema.yaml --output maxo.yaml source.ttl [...]
    maxo_to_linkml.py --report maxo.yaml validation-report.txt
"""

import argparse
import re
import sys
from collections import defaultdict

import rdflib
import yaml
from linkml_runtime.utils.schemaview import SchemaView
from rdflib import BNode, Graph, URIRef
from rdflib.namespace import OWL, RDF, RDFS, XSD

# Keep lexical forms as written (rdflib would otherwise rewrite e.g. ...Z to ...+00:00).
rdflib.NORMALIZE_LITERALS = False

OWL_AXIOM_PROPERTIES = {RDF.type, OWL.annotatedSource, OWL.annotatedProperty, OWL.annotatedTarget}
# Logical / structural predicates that are not part of the annotation layer.
# rdfs:subClassOf is handled separately (named parents only).
STRUCTURAL_PREDICATES = {
    RDF.type, OWL.equivalentClass, OWL.disjointWith, OWL.inverseOf, OWL.propertyChainAxiom,
    RDFS.domain, RDFS.range, RDFS.subPropertyOf, OWL.versionIRI, OWL.imports,
    OWL.members, OWL.distinctMembers, OWL.disjointUnionOf, OWL.someValuesFrom,
}
IRI_TYPES = {"uri", "uriorcurie", "curie", "nodeidentifier"}
OBO_PURL = "http://purl.obolibrary.org/obo/"
OBO_ID = re.compile(r"^([A-Z][A-Za-z]*)_(\d+)$")


class Converter:
    def __init__(self, schema_path):
        self.sv = SchemaView(schema_path)
        self.prefixes = sorted(
            ((p.prefix_prefix, p.prefix_reference) for p in self.sv.schema.prefixes.values()),
            key=lambda x: -len(x[1]),
        )
        self.root = next(c for c in self.sv.all_classes().values() if c.tree_root).name

    # -- naming -------------------------------------------------------------

    def curie(self, iri):
        """Contract an IRI; None if no prefix applies."""
        iri = str(iri)
        if iri.startswith(OBO_PURL):
            # Only real OBO ids, so obo/dcterms_creator never turns into dcterms:creator.
            m = OBO_ID.match(iri[len(OBO_PURL):])
            if m:
                return f"{m.group(1)}:{m.group(2)}"
        for pfx, ns in self.prefixes:
            if iri.startswith(ns) and pfx != "obo" and iri[len(ns):] and "/" not in iri[len(ns):]:
                return f"{pfx}:{iri[len(ns):]}"
        if iri.startswith(OBO_PURL):
            return f"obo:{iri[len(OBO_PURL):]}"
        return None

    def slot_map(self, class_name):
        """predicate IRI -> induced slot, for the slots of a class that have a slot_uri."""
        out = {}
        for slot in self.sv.class_induced_slots(class_name):
            if slot.slot_uri and not slot.identifier:
                out[URIRef(self.sv.expand_curie(slot.slot_uri))] = slot
        return out

    # -- values -------------------------------------------------------------

    def encode(self, node, range_name):
        expects_iri = range_name in IRI_TYPES or range_name in self.sv.all_enums()
        if isinstance(node, URIRef):
            if expects_iri:
                return self.curie(node) or str(node)
            return f"<{node}>" if range_name is not None else (self.curie(node) or str(node))
        if isinstance(node, BNode):
            return "_:blank"
        text = str(node)
        if node.datatype and node.datatype != XSD.string:
            text = f"{text}^^{self.curie(node.datatype) or '<' + str(node.datatype) + '>'}"
        elif node.language and node.language.lower() != "en":
            text = f"{text}@{node.language}"
        return f'"{text}"' if expects_iri else text

    def value_range(self, slot):
        """Range used to encode the main value of a slot (looks through annotated-value classes)."""
        if slot is None:
            return None
        if slot.range in self.sv.all_classes():
            return self.sv.induced_slot("value", slot.range).range
        return slot.range

    # -- graph walking ------------------------------------------------------

    def axiom_annotations(self, g):
        index = defaultdict(list)
        for ax in g.subjects(RDF.type, OWL.Axiom):
            key = (g.value(ax, OWL.annotatedSource), g.value(ax, OWL.annotatedProperty), g.value(ax, OWL.annotatedTarget))
            for p, o in g.predicate_objects(ax):
                if p not in OWL_AXIOM_PROPERTIES:
                    index[key].append((p, o))
        return index

    def group(self, pairs, smap, encode_value):
        """Group (predicate, object) pairs into a dict keyed by slot name (or CURIE if unknown).

        Single-valued slots get a scalar, unless there is more than one value: then a list
        is emitted so that the cardinality violation shows up in validation.
        """
        grouped = defaultdict(list)
        slots = {}
        for p, o in pairs:
            slot = smap.get(p)
            key = slot.name if slot else (self.curie(p) or str(p))
            slots[key] = slot
            grouped[key].append(encode_value(p, o, slot))
        out = {}
        for key, values in grouped.items():
            slot = slots[key]
            values = sorted(values, key=str)
            out[key] = values if (slot is None or slot.multivalued or len(values) > 1) else values[0]
        return out

    def annotations_to_object(self, value, pairs, class_name):
        """An annotation value plus its axiom annotations, keyed by the slots of class_name."""
        smap = self.slot_map(class_name) if class_name else {}
        rest = self.group(pairs, smap, lambda p, o, slot: self.encode(o, slot.range if slot else None))
        return {"value": value, **rest}

    def entity(self, g, s, smap, axanns):
        def encode_value(p, o, slot):
            encoded = self.encode(o, self.value_range(slot))
            anns = axanns.get((s, p, o), [])
            rng = slot.range if slot else None
            if rng in self.sv.all_classes():
                return self.annotations_to_object(encoded, anns, rng)
            if anns:
                # Axiom annotations on a plain-valued slot: emitted, so the schema can reject them.
                return self.annotations_to_object(encoded, anns, None)
            return encoded

        pairs = [(p, o) for p, o in g.predicate_objects(s)
                 if p not in STRUCTURAL_PREDICATES and not isinstance(o, BNode)]
        return dict(sorted(self.group(pairs, smap, encode_value).items()))

    def convert(self, g):
        axanns = self.axiom_annotations(g)
        ontologies = [o for o in g.subjects(RDF.type, OWL.Ontology) if isinstance(o, URIRef)]
        if len(ontologies) != 1:
            sys.exit(f"Expected exactly one owl:Ontology, found {len(ontologies)}")
        ont = ontologies[0]

        doc = {"id": self.curie(ont) or str(ont)}
        doc.update(self.entity(g, ont, self.slot_map(self.root), axanns))

        term_class = self.sv.induced_slot("terms", self.root).range
        term_smap = self.slot_map(term_class)
        subjects = set()
        for s, p, o in g:
            if not isinstance(s, URIRef) or s == ont:
                continue
            if p in STRUCTURAL_PREDICATES or p == RDFS.subClassOf or isinstance(o, BNode):
                # Declarations and logic alone do not make a term, except for MAXO's own classes.
                if not (str(s).startswith(OBO_PURL + "MAXO_") and o == OWL.Class):
                    continue
            subjects.add(s)
        doc["terms"] = [
            {"id": self.curie(s) or str(s), **self.entity(g, s, term_smap, axanns)}
            for s in sorted(subjects)
        ]
        return doc


def rewrite_report(data_path, report_path):
    """Replace /terms/<n> in a linkml-validate report with the term id, in place."""
    with open(data_path) as fh:
        ids = [t["id"] for t in yaml.safe_load(fh)["terms"]]
    with open(report_path) as fh:
        report = fh.read()
    report = re.sub(r"/terms/(\d+)", lambda m: f"/terms/{ids[int(m.group(1))]}", report)
    with open(report_path, "w") as fh:
        fh.write(report)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("inputs", nargs="*", help="RDF files (any rdflib-readable format, e.g. Turtle)")
    parser.add_argument("--schema")
    parser.add_argument("--output", "-o")
    parser.add_argument("--report", nargs=2, metavar=("DATA_YAML", "REPORT"),
                        help="Instead of converting: rewrite /terms/<n> in a linkml-validate report to term ids")
    args = parser.parse_args()

    if args.report:
        rewrite_report(*args.report)
        return
    if not (args.inputs and args.schema and args.output):
        parser.error("inputs, --schema and --output are required for conversion")
    g = Graph()
    for path in args.inputs:
        g.parse(path)
    doc = Converter(args.schema).convert(g)
    with open(args.output, "w") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, allow_unicode=True, width=1000)


if __name__ == "__main__":
    main()
