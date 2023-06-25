import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dna_complement import Complement

# Test case
dna_sequence = "ATCG"
complement_sequence = Complement(dna_sequence)
expected_result = "TAGC"

# Check if the complement sequence matches the expected result
if complement_sequence == expected_result:
        print("Test case passed!")
else:
        print("Test case failed. Expected:", expected_result, "but got:", complement_sequence)

