import xml.etree.ElementTree as ET
import glob
import os


def extract_text_from_p(element):
    """ Extract texts from elements with a tag "p"

    The function will remove html tags within the text of Element p.
    example:
    "The reason for this is that an autosomal copy of
    <italic toggle="yes">DAZ</italic> (<italic toggle="yes">DAZL</italic>) may serve ..."
    should be
    "The reason for this is that an autosomal copy of
    DAZ (DAZL) may serve ..."

    :param element: should be an element with a tag of "p"
    :return: all texts under the element
    """
    #

    return ''.join(element.itertext())


def extract_sec(section):
    """ Extract information at the second bottom level

    The bottom level is <title>, <p>, <list> with title being categories of treatment and p being descriptions.
    One level above it is the entire "Management" section, as well as "Diagnosis", "Clinical_Characteristics",
    "Genetically_Related_Disorders", "Differential_Diagnosis", "Genetic_Counseling", etc. The function should
    work for all those sections (TO be tested).

    :param section: should be the "Management" section in the body
    :return: all texts under the section, including titles.
    """
    extractedText = ''
    for child in section.iter():
        if (child.tag == 'p'):
            extractedText = extractedText + "\n\n" + extract_text_from_p(child).rstrip()
        if (child.tag == 'title'):
            extractedText = extractedText + '\n\n' + child.text.lstrip() + '\n\n'
        if (child.tag == 'table-wrap'):
            extractedText = extractedText + '\n\n' + extract_text_from_p(child).rstrip() + '\n\n'
    return extractedText


def extract_Management(filepath):
    """Extract texts within the "Management" section

    Uses the above methods to extract information under the "Management" section

    :param filepath: to the location of xml files
    :return: extracted text
    """
    tree = ET.parse(filepath)
    disease = disease_name(filepath)
    extractedText = ''
    for elem in tree.iterfind('./book-part/body/sec'):
        # The attrib for "Management" is "(name of disease).Management" (652 diseases)
        # or "(name of disease).Management_1" (40 diseases)
        # or "(name of disease).Acute_Management_of_a_Urea" (1 diseases, ucd-overview)
        # or "(name of disease).Management_of_Nonsyndromic_R" (1 diseases, rp-overview)
        if (elem.get('id') == disease + ".Management" or elem.get('id') == disease + ".Management_1" \
            or elem.get('id') == disease + ".Acute_Management_of_a_Urea" \
                    or elem.get('id') == disease + ".Management_of_Nonsyndromic_R"):
            extractedText = extract_sec(elem)
    return extractedText


def disease_name(filepath):
    """ Extract the name of a disease from the filepath of xml files.

    The name of a disease is used in forming the attributes of the Management section,
    url to the webpage and naming the extract text file.

    :param filepath: location of the xml file
    :return: name of the disease
    """
    path_split = filepath.split('/')
    # disease name will be in the last item, such as 'yci.nxml'
    name_pos = len(path_split) - 1
    return path_split[name_pos].split('.')[0]

def gene_NBKid():
    """
    Returns a dictionary of relationships between gene symbols and NBKid
    :return:
    """
    gene_NBKid_dict = {}
    with open('../GRtitle_shortname_NBKid.txt', 'r', encoding='latin') as file:
        for line in file.readlines():
            elem = line.split('\t')
            gene = elem[0]
            NBKid = elem[2]
            if gene not in gene_NBKid_dict.keys():
                gene_NBKid_dict[gene] = NBKid
            else:
                if gene_NBKid_dict[gene] != NBKid:
                    print('one gene corresponds to multiple NBKid!')
    return gene_NBKid_dict

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

        lines = []
        for line in extracted.split('\n'):
            lines.append(line.lstrip())
        extracted_formated = '\n'.join(lines)

        url = "http://www.ncbi.nlm.nih.gov/books/n/gene/" + disease_name(file)
        if (not extracted == ''):
            export = open(export_path, 'w+')
            export.write(url)
            export.write(extracted_formated)
            export.close()




