"""
Reverse of a DNA sequence.
"""


def reverse(dna_sequence):
    """
    Reverse the given DNA sequence.

    Args:
    dna_sequence (str): The DNA sequence.

    Returns:
    str: The reversed sequence.

    """
    reverse_sequence = ""
    for char in dna_sequence:
        reverse_sequence = char + reverse_sequence
    return reverse_sequence
