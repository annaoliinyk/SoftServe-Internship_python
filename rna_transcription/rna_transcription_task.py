# Task from https://exercism.org/tracks/python/exercises/rna-transcription

def to_rna(dna_strand):
    switch = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    result = ''
    for letter in dna_strand:
        result += switch.get(letter, "")
    return result
