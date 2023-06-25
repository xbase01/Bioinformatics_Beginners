"""
Write a function ReverseComplement() to solve the Reverse Complement Problem, 
which is reproduced below. (Remember that we have already given you this 
code at the beginning of the module.)
"""

from reverse_dna import reverse
from dna_complement import Complement


def reversecomplement(dna_sequence):
    """
    Calculate the reverse complement of a DNA sequence pattern.

    Args:
        dna_sequence (str): The DNA sequence pattern.

    Returns:
        str: The reverse complement of the pattern.
    """

    reverse_sequence = reverse(dna_sequence)
    reverse_complement = Complement(reverse_sequence)
    return reverse_complement
