# Task taken from https://exercism.org/tracks/python/exercises/acronym
import logging

logging.basicConfig(level=logging.INFO)


def abbreviate(words: str):
    try:
        result = ""
        words_as_list = split_phrase(words)
        for word in words_as_list:
            try:
                result += word[0].upper()
            # if it can't be converted to upper, it's probably " "
            except:
                continue
        return result
    except:
        logging.error("Invalid input")


def split_phrase(phrase):
    words_list = phrase.split(" ")
    return words_list


def main():
    logging.info(abbreviate("Halley's Comet"))  # expected: "HC"
    logging.info(abbreviate("Halley's    Comet"))  # expected: "HC"
    logging.info(abbreviate(["Jj"]))  # expected: error


if __name__ == "__main__":
    main()
