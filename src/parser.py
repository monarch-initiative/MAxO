#!/usr/bin/python
import xml.etree.ElementTree as ET

tree = ET.parse('../resource/gene_NBK1116/yci.nxml')
root = tree.getroot()
print(root)
body = root.find('./book-part/body')
for child in list(body):
    if(child.get('id')=='yci.Management'):
        management = child
        for child in list(management):
            if(child.tag=='title'):
                print(child.text)
            if(child.tag=='sec'):
                for sec_child in child:
                    print (sec_child.text)
