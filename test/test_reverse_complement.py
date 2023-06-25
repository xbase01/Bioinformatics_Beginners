import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now you can import the reverse function

from dna_reverse_complement import reversecomplement

# Test case
dna_sequence = "ATCG"
expected_result = "CGAT"
reverse_complement = reversecomplement(dna_sequence)

if reverse_complement == expected_result:
        print("Test case passed!")
else:
        print(f"Test case failed. Expected: {expected_result}. Got: {reverse_complement}.")
