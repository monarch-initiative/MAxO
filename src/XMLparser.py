import xml.etree.ElementTree as ET

# It removes html links in texts (example: The reason for this is that an autosomal
# copy of <italic toggle="yes">DAZ</italic> (<italic toggle="yes">DAZL</italic>) may serve ...)
def extract_text_from_p(element):
    return ''.join(element.itertext())

# It extract an entire section from one section of GeneReviews book-part/body
# Aside yci.Management, it can also extract yci.Diagnosis, yci.Clinical_Characteristics,
# yci.Genetically_Related_Disorders, yci.Differential_Diagnosis, yci.Genetic_Counseling,
# yci.Resources etc (not tested yet)
def extract_sec(section):
    for child in section.iter():
        if (child.tag == 'p'):
            print(extract_text_from_p(child))
        if (child.tag == 'title'):
            print('\n' + child.text + '\n')


def extract_Management(filepath):
    tree = ET.parse(filepath)
    disease = disease_name(filepath)
    for elem in tree.iterfind('./book-part/body/sec'):
        if (elem.get('id') == disease + ".Management"):
            management = elem
            extract_sec(management)


# It extract the name of the disease from it's xml filepath.
def disease_name(filepath):
    return filepath.split('/')[6].split('.')[0]


filepath = '/Users/zhangx/MAO/resource/gene_NBK1116/xq28-dup.nxml'
filepath = '/Users/zhangx/MAO/resource/gene_NBK1116/xlmr.nxml'
filepath = '/Users/zhangx/MAO/resource/gene_NBK1116/TOC.nxml'

extract_Management(filepath)



