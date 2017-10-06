import glob


def get_texts_between(filepath, start_line, end_line):
    """
    Extract text between two lines

    :param filepath: path to the target file
    :param start_line: starting line (exclusive)
    :param end_line: ending line (exclusive)
    :return: lines between the starting line and ending line (exclusive)
    """
    management = open(filepath)
    evaluation_initial_diagonosis = []
    in_range = False
    for line in iter(management):
        if line.strip() == start_line.strip():
            in_range = True
        if line.strip() == end_line.strip():
            break
        # remove empty lines and starting lines
        if in_range and line.strip() != start_line and line.strip():
            evaluation_initial_diagonosis.append(line)
    management.close()
    return '\n'.join(evaluation_initial_diagonosis)


def main():
    start_line = 'Evaluations Following Initial Diagnosis'
    end_line = 'Treatment of Manifestations'
    try:
        Evaluation_initial_Diagnosis = open('../Evaluation_initial_Diagnosis_all_disease.txt', 'w')
    except OSError:
        print('Cannot create file')
    all_files = glob.glob('../Gene_Reviews_Extracted/*.txt')
    for file in all_files:
        Evaluation_initial_Diagnosis.write(get_texts_between(file, start_line, end_line))
    Evaluation_initial_Diagnosis.close()


if __name__ == '__main__':
    main()