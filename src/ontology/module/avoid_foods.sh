#!/bin/bash
dosdp-tools generate \
--obo-prefixes=true \
--prefixes=../pattern/prefixes.yaml \
--table-format=CSV \
--template=../pattern/avoid_consumption_of_foods.yaml \
--infile=avoid_foods.csv \
--outfile=avoid_consumption_of_foods.ofn
