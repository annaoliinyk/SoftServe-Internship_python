# Task from https://exercism.org/tracks/python/exercises/house

import logging

logging.basicConfig(level=logging.INFO)

RHYME_LINES_LIST = ["the house that Jack built.",
                    "the malt that lay in ",
                    "the rat that ate ",
                    "the cat that killed ",
                    "the dog that worried ",
                    "the cow with the crumpled horn that tossed ",
                    "the maiden all forlorn that milked ",
                    "the man all tattered and torn that kissed ",
                    "the priest all shaven and shorn that married ",
                    "the rooster that crowed in the morn that woke ",
                    "the farmer sowing his corn that kept ",
                    "the horse and the hound and the horn that belonged to "]


def recite(start_verse: int, end_verse: int):
    try:
        result = []
        for i in range(start_verse, end_verse + 1):
            result.append(get_full_line(i))
        return result
    except:
        logging.error("Invalid input")


def get_full_line(line_number: int):
    if 0 < line_number <= len(RHYME_LINES_LIST):
        result = "This is "
        # get only needed parts of the final line from RHYME_LINES_LIST
        needed_parts_list = (RHYME_LINES_LIST[:line_number])
        # reverse this needed lines list, to write the parts in a correct order
        needed_parts_list.reverse()
        for part in needed_parts_list:
            result += part
        return result


def main():
    logging.info(recite(2, 2))
    logging.info(recite(1, 5))
    logging.info(recite(12, 12))
    logging.info(recite(0, 0))  # None expected


if __name__ == "__main__":
    main()
