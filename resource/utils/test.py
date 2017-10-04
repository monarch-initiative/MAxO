import os
import glob
files_to_parse = glob.glob("../gene_NBK1116/*.nxml")
for file in files_to_parse:
    print(file)
print(os.getcwd())