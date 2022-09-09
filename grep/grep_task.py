# Task from https://exercism.org/tracks/python/exercises/grep
import logging

logging.basicConfig(level=logging.INFO)


def grep(pattern: str, flags: str, files: list):
    try:
        # if -i in flags - will ignore case while finding matched parts
        if "-i" in flags:
            pattern = pattern.lower()
        result, non_matching_lines = "", ""
        first_file = files[0]
        # checking if one file provided, many files, or no files
        if len(files) == 1:
            # try to open file; if doesn't exist - program will stop and return None
            try:
                datafile = get_data_from_file(first_file)
            except:
                logging.error("Provided file does not exist")
                return None
            line_counter = 1
            for line in datafile:
                # iterate through lines to find matching lines per given flags
                result, non_matching_lines = get_matched_one_file(line_counter, line, pattern, result, flags,
                                                                  non_matching_lines)
                line_counter += 1
        elif len(files) > 1:
            for file in files:
                # try to open file; if doesn't exist - program will print error and file name
                try:
                    datafile = get_data_from_file(file)
                    line_counter = 1
                    for line in datafile:
                        line_to_match = line
                        if "-i" in flags:
                            line_to_match = line.lower()
                        # if -x in flags - only match entire lines, instead of lines that contain a match
                        if "-x" in flags:
                            if pattern + "\n" == line_to_match and "-n" in flags:
                                result += file + ":" + str(line_counter) + ":" + line
                            elif pattern + "\n" == line_to_match:
                                result += file + ":" + line
                            # if -v: collect all lines that fail to match the pattern
                            elif "-v" in flags:
                                non_matching_lines += file + ":" + line
                        else:
                            if pattern in line_to_match and "-n" in flags:
                                result += file + ":" + str(line_counter) + ":" + line
                            elif pattern in line_to_match:
                                result += file + ":" + line
                            # if -v: collect all lines that fail to match the pattern
                            elif "-v" in flags:
                                if "-n" in flags:
                                    non_matching_lines += file + ":" + str(line_counter) + ":" + line
                                else:
                                    non_matching_lines += file + ":" + line
                        line_counter += 1
                except:
                    logging.error(f"Provided file {file} does not exist")
        else:
            return ""

        if "-l" not in flags and "-v" not in flags:
            return result
        # if -v: collect all lines that fail to match the pattern
        elif "-v" in flags:
            return non_matching_lines
        elif "-l" in flags:
            return return_filenames(first_file, result, len(files))
    except:
        logging.error("Invalid input")


def get_matched_one_file(line_counter, line, pattern, result, flags, non_matching_lines=""):
    line_to_match = line
    if "-i" in flags:
        line_to_match = line.lower()
    # if -x in flags - only match entire lines, instead of lines that contain a match
    if "-x" in flags:
        if pattern + "\n" == line_to_match and "-n" in flags:
            result += str(line_counter) + ":" + line
        elif pattern + "\n" == line_to_match:
            result += line
        # if -v: collect all lines that fail to match the pattern
        elif "-v" in flags:
            non_matching_lines += line
    else:
        if pattern in line_to_match and "-n" in flags:
            result += str(line_counter) + ":" + line
        elif pattern in line_to_match:
            result += line
        # if -v: collect all lines that fail to match the pattern
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


def return_filenames(first_file, result, files_number):
    if not result:
        return ""
    elif files_number == 1:
        return first_file + "\n"
    else:
        files_as_result = ""
        result_as_list = result.split("\n")
        for line in result_as_list:
            first_filename = line.split(":")[0]
            if first_filename not in files_as_result:
                files_as_result += first_filename + "\n"
        return files_as_result
