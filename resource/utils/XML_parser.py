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
    return ''.join(element.itertext())


def extract_sec(section):
    """ Extract information at the second bottom level

    The bottom level is <title>, <p> with title being categories of treatment and p being descriptions.
    One level above it is the entire "Management" section, as well as "Diagnosis", "Clinical_Characteristics",
    "Genetically_Related_Disorders", "Differential_Diagnosis", "Genetic_Counseling", etc. The function should
    work for all those sections (TO be tested).

    :param section: should be the "Management" section in the body
    :return: all texts under the section, including titles.
    """
    extractedText = ''
    for child in section.iter():
        if (child.tag == 'p'):
            extractedText = extractedText + " " + extract_text_from_p(child).rstrip()
        if (child.tag == 'title'):
            extractedText = extractedText + '\n\n' + child.text.lstrip() + '\n\n'
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
        # The attrib for "Management" is "(name of disease).Management"
        if (elem.get('id') == disease + ".Management"):
            extractedText = extract_sec(elem)
    return extractedText


def disease_name(filepath):
    """ Extract the name of a disease from the filepath of xml files.

    The name of a disease is used in forming the attributes of the Management section,
    url to the webpage and naming the extract text file.

    :param filepath: location of the xml file
    :return: name of the disease
    """
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
        url = "http://www.ncbi.nlm.nih.gov/books/n/gene/" + disease_name(file)
        if (not extracted == ''):
            export = open(export_path, 'w+')
            export.write(url)
            export.write(extracted)
            export.close()




