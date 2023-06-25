import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dna_pattern_matching import PatternMatching

# Test 0: Sample Dataset
pattern0 = "ATAT"
genome0 = "GATATATGCATATACTT"
expected_output0 = [1, 3, 9]
assert PatternMatching(pattern0, genome0) == expected_output0

# Test 1: Not counting Reverse Complements
pattern1 = "ACAC"
genome1 = "TTTTACACTTTTTTGTGTAAAAA"
expected_output1 = [4]
assert PatternMatching(pattern1, genome1) == expected_output1

# Test 2: Pattern at the beginning of Genome
pattern2 = "AAA"
genome2 = "AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT"
expected_output2 = [0, 46, 51, 74]
assert PatternMatching(pattern2, genome2) == expected_output2

# Test 3: Pattern at the end of Genome
pattern3 = "TTT"
genome3 = "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"
expected_output3 = [88, 92, 98, 132]
assert PatternMatching(pattern3, genome3) == expected_output3

# Test 4: Overlapping occurrences of Pattern
pattern4 = "ATA"
genome4 = "ATATATA"
expected_output4 = [0, 2, 4]
assert PatternMatching(pattern4, genome4) == expected_output4

print("All test cases passed!")
