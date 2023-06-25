"""
Write a function Complement() that takes a DNA string Pattern and returns 
a string formed by taking the complement of each letter of Pattern
"""
def Complement(dna_sequence):
    """
    Generate the complement of a DNA sequence.

    Args:
        dna_sequence (str): The DNA sequence pattern.

    Returns:
        str: The complement of the DNA sequence.
    """

    complement_sequence = ""
    for nucleotide in dna_sequence:
        if nucleotide == 'A':
            complement_sequence += 'T'
        elif nucleotide == 'T':
            complement_sequence += 'A'
        elif nucleotide == 'C':
            complement_sequence += 'G'
        elif nucleotide == 'G':
            complement_sequence += 'C'
    return complement_sequence
