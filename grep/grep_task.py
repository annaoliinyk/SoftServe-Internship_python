# Task from https://exercism.org/tracks/python/exercises/grep

def grep(pattern, flags, files):
    if "-i" in flags:
        pattern = pattern.lower()
    result, non_matching_lines = "", ""

    if len(files) == 1:
        datafile = get_data_from_file(files[0])
        line_counter = 1
        for line in datafile:
            result, non_matching_lines = get_matching_lines_single_file(line_counter, line, pattern, result, flags,
                                                                        non_matching_lines)
            line_counter += 1
    elif len(files) > 1:
        for i in range(len(files)):
            datafile = get_data_from_file(files[i])
            line_counter = 1
            for line in datafile:
                line_to_match = line
                if "-i" in flags:
                    line_to_match = line.lower()
                if "-x" in flags:
                    if pattern + "\n" == line_to_match and "-n" in flags:
                        result += files[i] + ":" + str(line_counter) + ":" + line
                    elif pattern + "\n" == line_to_match:
                        result += files[i] + ":" + line
                    elif "-v" in flags:
                        non_matching_lines += files[i] + ":" + line
                else:
                    if pattern in line_to_match and "-n" in flags:
                        result += files[i] + ":" + str(line_counter) + ":" + line
                    elif pattern in line_to_match:
                        result += files[i] + ":" + line
                    elif "-v" in flags:
                        if "-n" in flags:
                            non_matching_lines += files[i] + ":" + str(line_counter) + ":" + line
                        else:
                            non_matching_lines += files[i] + ":" + line
                line_counter += 1

    if "-l" not in flags and "-v" not in flags:
        return result
    elif "-v" in flags:
        return non_matching_lines

    elif "-l" in flags:
        return return_filenames(files, result)


def get_matching_lines_single_file(line_counter, line, pattern, result, flags, non_matching_lines=""):
    line_to_match = line
    if "-i" in flags:
        line_to_match = line.lower()
    if "-x" in flags:
        if pattern + "\n" == line_to_match and "-n" in flags:
            result += str(line_counter) + ":" + line
        elif pattern + "\n" == line_to_match:
            result += line
        elif "-v" in flags:
            non_matching_lines += line
    else:
        if pattern in line_to_match and "-n" in flags:
            result += str(line_counter) + ":" + line
        elif pattern in line_to_match:
            result += line
        elif "-v" in flags:
            if "-n" in flags:
                non_matching_lines += str(line_counter) + ":" + line
            else:
                non_matching_lines += line

    return result, non_matching_lines


def get_data_from_file(file_name):
    with open(file_name) as temp_f:
        datafile = temp_f.readlines()
    return datafile


def return_filenames(files, result):
    if not result:
        return ""
    elif len(files) == 1:
        return files[0] + "\n"
    else:
        files_as_result = ""
        for line in result.split("\n"):
            if line.split(":")[0] not in files_as_result:
                files_as_result += line.split(":")[0] + "\n"
        return files_as_result
