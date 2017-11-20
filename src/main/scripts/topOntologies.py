from collections import defaultdict
from ExtractMostFrequentSens import order_dictionary, dict_to_file
import os
import glob

outdir = "../resources/Ontology_Terms/Most_Frequent_Oncologies_UMLSxref"
try:
    os.mkdir(outdir)
except FileExistsError:
    pass


def onco_name(source):
    if source.strip():
        elems = source.strip().split('//')
    return elems[2]


def onco_freq(infile):
    file_name = infile.split('/')[-1]
    if file_name.startswith("most_frequent_10_"):
        file_name = file_name[17:]
    outfile = outdir + "/" + file_name
    onco_freq = defaultdict(int)
    with open(infile, 'r') as infile:
        for line in infile.readlines():
            oncos = line.strip('\n').split("\t")[1:]
            for record in oncos:
                if record.strip():
                    onco_freq[onco_name(record)] += 1
    print(onco_freq['CHV'])
    onco_freq = order_dictionary(onco_freq)
    dict_to_file(onco_freq, outfile)


def main():
    infiles = glob.glob("../resources/Ontology_Terms/Most_Frequent_Sens_and_UMLSxref/*.txt")
    for file in infiles:
        onco_freq(file)

if __name__ == '__main__':
    main()
