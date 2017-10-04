import xml.etree.ElementTree as ET
import glob
import os

# It removes html links in texts (example: The reason for this is that an autosomal
# copy of <italic toggle="yes">DAZ</italic> (<italic toggle="yes">DAZL</italic>) may serve ...)
def extract_text_from_p(element):
    return ''.join(element.itertext())

# It extract an entire section from one section of GeneReviews book-part/body
# Aside yci.Management, it can also extract yci.Diagnosis, yci.Clinical_Characteristics,
# yci.Genetically_Related_Disorders, yci.Differential_Diagnosis, yci.Genetic_Counseling,
# yci.Resources etc (not tested yet)
def extract_sec(section):
    extractedText = ''
    for child in section.iter():
        if (child.tag == 'p'):
            extractedText = extractedText + " " + extract_text_from_p(child)
        if (child.tag == 'title'):
            extractedText = extractedText + '\n\n' + child.text + '\n\n'
    return extractedText

# It extracts all texts from the Management section, excluding links in the texts
def extract_Management(filepath):
    tree = ET.parse(filepath)
    disease = disease_name(filepath)
    extractedText = ''
    for elem in tree.iterfind('./book-part/body/sec'):
        if (elem.get('id') == disease + ".Management"):
            extractedText = extract_sec(elem)
    return extractedText


# It extract the name of the disease from it's xml filepath.
def disease_name(filepath):
    return filepath.split('/')[2].split('.')[0]


if __name__ == "__main__":
    files_to_parse = glob.glob("../gene_NBK1116/*.nxml")
    try:
        os.mkdir("../Gene_Reviews_Extracted")
    except FileExistsError:
        pass
    EXPORT_FOLDER = '../Gene_Reviews_Extracted/'
    for file in files_to_parse:
        export_path = EXPORT_FOLDER + disease_name(file) + '.txt'
        extracted = extract_Management(file)
        if (not extracted == ''):
            export = open(export_path, 'w+')
            export.write(extracted)
            export.close()




