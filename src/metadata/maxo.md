---
layout: ontology_detail
id: maxo
title: Medical Action Ontology
jobs:
  - id: https://travis-ci.org/monarch-initiative/MAxO
    type: travis-ci
build:
  checkout: git clone https://github.com/monarch-initiative/MAxO.git
  system: git
  path: "."
contact:
  email: 
  label: 
  github: 
description: Medical Action Ontology is an ontology...
domain: stuff
homepage: https://github.com/monarch-initiative/MAxO
products:
  - id: maxo.owl
    name: "Medical Action Ontology main release in OWL format"
  - id: maxo.obo
    name: "Medical Action Ontology additional release in OBO format"
  - id: maxo.json
    name: "Medical Action Ontology additional release in OBOJSon format"
  - id: maxo/maxo-base.owl
    name: "Medical Action Ontology main release in OWL format"
  - id: maxo/maxo-base.obo
    name: "Medical Action Ontology additional release in OBO format"
  - id: maxo/maxo-base.json
    name: "Medical Action Ontology additional release in OBOJSon format"
dependencies:
- id: iao
- id: go
- id: ro
- id: uberon

tracker: https://github.com/monarch-initiative/MAxO/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
activity_status: active
---

Enter a detailed description of your ontology here. You can use arbitrary markdown and HTML.
You can also embed images too.

