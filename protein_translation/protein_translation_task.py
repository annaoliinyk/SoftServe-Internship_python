# Task from https://exercism.org/tracks/python/exercises/protein-translation

switcher = {
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
stop_codons = ["UAA", "UAG", "UGA"]


def proteins(strand):
    codons_list = get_codons_list(strand)
    proteins_list = []
    for codon in codons_list:
        if codon in stop_codons:
            return proteins_list
        protein = switcher.get(codon)
        proteins_list.append(protein)
    return proteins_list


def get_codons_list(strand):
    codons_list = []
    for i in range(0, len(strand), 3):
        codons_list.append(strand[i:i + 3])
    return codons_list
