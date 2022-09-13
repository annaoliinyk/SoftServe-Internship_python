# Task from https://exercism.org/tracks/python/exercises/rna-transcription

import logging

logging.basicConfig(level=logging.INFO)

SWITCHER = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}


def to_rna(dna_strand: str):
    try:
        result = ''
        for letter in dna_strand:
            result += SWITCHER.get(letter.upper(), "")
        return result
    except:
        logging.error("Invalid input")


def main():
    logging.info(to_rna(""))  # expected: ""
    logging.info(to_rna("C"))  # expected: "G"
    logging.info(to_rna("G"))  # expected: "C"
    logging.info(to_rna("ACGTGGTCTTAA"))  # expected: "UGCACCAGAAUU"


if __name__ == "__main__":
    main()
