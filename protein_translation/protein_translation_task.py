# Task from https://exercism.org/tracks/python/exercises/protein-translation

def proteins(strand):
    codons_list = get_codors_list(strand)
    proteins_list = []
    for codon in codons_list:
        if codon in ["UAA", "UAG", "UGA"]:
            return proteins_list
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
        protein = switcher.get(codon)
        proteins_list.append(protein)
    return proteins_list


def get_codors_list(strand):
    codons_list = []
    for i in range(0, len(strand), 3):
        codons_list.append(strand[i:i + 3])
    return codons_list
