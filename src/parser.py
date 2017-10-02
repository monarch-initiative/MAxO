#!/usr/bin/python
import xml.etree.ElementTree as ET

tree = ET.parse('../resource/gene_NBK1116/yci.nxml')
root = tree.getroot()
print(root)


