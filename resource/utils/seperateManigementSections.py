import glob
import os
from XML_parser import disease_name

# This script seperates the Management section of all diseases into subsections
# including 'Evaluations Following Initial Diagnosis',
#           'Treatment of Manifestations',
#           'Prevention of Primary Manifestations',
#           'Prevention of Secondary Complications',
#           'Surveillance',
#           'Agents/Circumstances to Avoid',
#           'Evaluation of Relatives at Risk',
#           'Therapies Under Investigation'
# for each subsection, there is a file that contains texts from all diseases and a folder that contains
# texts of each disease in a single file

# order matters!
section_lines = ['Evaluations Following Initial Diagnosis',
                 'Treatment of Manifestations',
                 'Prevention of Primary Manifestations',
                 'Prevention of Secondary Complications',
                 'Surveillance',
                 'Agents/Circumstances to Avoid',
                 'Evaluation of Relatives at Risk',
                 'Therapies Under Investigation']

all_files = glob.glob('../Gene_Reviews_Extracted/*.txt')


def get_texts_between(filepath, start_line, end_lines):
    """
    Extract text between two lines

    :param filepath: path to the target file
    :param start_line: starting line (exclusive)
    :param end_lines: ending line (exclusive)
    :return: lines between the starting line and ending line (exclusive)
    """
    management = open(filepath)
    evaluation_initial_diagonosis = []
    in_range = False
    for line in iter(management):
        if line.strip() == start_line.strip():
            in_range = True
        if line.strip() in [elem.strip() for elem in end_lines]:
            break
        # remove empty lines and starting lines
        if in_range and line.strip() != start_line and line.strip():
            evaluation_initial_diagonosis.append(line)
    management.close()
    return '\n'.join(evaluation_initial_diagonosis)


def section_of_management_all_disease():
    """
    Divide the Management of each disease into subsections,
    and combine the same subsections of all diseases into a single file.
    """
    new_folder = '../Gene_Reviews_Extracted/Sections_combined/'
    if not os.path.isdir(new_folder):
        os.mkdir(new_folder)
    paths = [''.join([new_folder, str.replace('/', '_').replace(' ', '_'),
                      '_all_diseases.txt']) for str in section_lines[:len(section_lines) - 1]]

    for i in range(len(paths)):
        with open(paths[i], 'w') as file_to_write_to:
            for file in all_files:
                    file_to_write_to.write(get_texts_between(file, section_lines[i], section_lines[(i + 1) :]))


def section_of_management_individual():
    """
    Divide the Management of each disease into sebsections,
    and save each subsection in invidual files.

    """
    folders = [''.join(['../Gene_Reviews_Extracted/', str.replace('/', '_').replace(' ', '_'), '/'])
               for str in section_lines[:len(section_lines) - 1]]
    print(folders)

    prefixs = ['initial___', 'manifestation___', 'prevention1___','prevention2___', 'surveillance___', 'avoidance___',
               'relatives___'] # 7 folders
    print(prefixs)
    for i in range(len(folders)):
        if not os.path.isdir(folders[i]):
            os.mkdir(folders[i])
        for file in all_files:
            path_to_file = ''.join([folders[i], prefixs[i], disease_name(file), '.txt'])
            with open(path_to_file, 'w') as file_to_write_to:
                file_to_write_to.write(get_texts_between(file, section_lines[i], section_lines[(i + 1) : ]))


def all_section_of_management_in_one():
    """
    Combine the Management section of each disease into one single file.

    """
    with open('../management_all_disease.txt', 'a') as entire_management:
        for file in all_files:
            entire_management.write(get_texts_between(file, section_lines[0], ['***************']))


if __name__ == '__main__':
    section_of_management_individual()
    section_of_management_all_disease()
    all_section_of_management_in_one()
