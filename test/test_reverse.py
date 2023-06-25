import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now you can import the reverse function
from reverse_dna import reverse


# Test case 1
dna_sequence_1 = "ATCG"
reversed_sequence_1 = reverse(dna_sequence_1)
print("Test case 1:")
print("Original sequence:", dna_sequence_1)
print("Reversed sequence:", reversed_sequence_1)

# Test case 2
dna_sequence_2 = "GATTACA"
reversed_sequence_2 = reverse(dna_sequence_2)
print("Test case 2:")
print("Original sequence:", dna_sequence_2)
print("Reversed sequence:", reversed_sequence_2)
