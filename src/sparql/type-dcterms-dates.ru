# Types dcterms:date values as xsd:dateTime. DOSDP writes every text annotation
# as xsd:string, so pattern-generated dates are retyped here after generation.
# Only values that are valid UTC timestamps are touched.

PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

DELETE { ?s dcterms:date ?date }
INSERT { ?s dcterms:date ?typed }
WHERE {
  ?s dcterms:date ?date .
  FILTER(isLiteral(?date) && datatype(?date) = xsd:string)
  FILTER(regex(str(?date), "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"))
  BIND(STRDT(str(?date), xsd:dateTime) AS ?typed)
}
