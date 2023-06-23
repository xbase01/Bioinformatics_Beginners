#!/usr/bin/python3
"""
Algorithm that counts the number of K-mer in a DNA sequence when
searching for the hidden messages in the replication origin
"""


def PatternCount(pattern, sequence):

    counter = 0
    for i in range(len(sequence)):
        if sequence.startswith(pattern, i):
            counter += 1
            # this will count the occurrence
    return counter


print(PatternCount("ATA", "CGATATATCCATAG"))

# OR


def patternCount(pattern, text):

    count = 0
    last_position = len(text) - len(pattern) + 1
    # lets iteration i know when to stop must not count till the last text

    for i in range(last_position):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count


pattern = "TGATCA"
text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

print(patternCount(pattern, text))
