# Task from https://exercism.org/tracks/python/exercises/protein-translation

import logging

logging.basicConfig(level=logging.INFO)

SWITCHER = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan"
}
STOP_CODONS = ["UAA", "UAG", "UGA"]


def proteins(strand: str):
    try:
        codons_list = get_codons_list(strand)
        proteins_list = []
        for codon in codons_list:
            if codon in STOP_CODONS:
                return proteins_list
            protein = SWITCHER.get(codon)
            proteins_list.append(protein)
        return proteins_list
    except:
        logging.error("Invalid input")


def get_codons_list(strand):
    codons_list = []
    for i in range(0, len(strand), 3):
        codons_list.append(strand[i:i + 3])
    return codons_list


def main():
    logging.info(proteins("UCG"))  # expected: ["Serine"]
    logging.info(proteins("UAA"))  # expected: []
    logging.info(proteins("UGGUAGUGG"))  # expected: ["Tryptophan"]
    logging.info(proteins(["UGC", "UUG"]))  # expected: error logging message


if __name__ == "__main__":
    main()
