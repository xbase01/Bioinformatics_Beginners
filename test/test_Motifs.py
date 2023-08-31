import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the function to be tested
from Motifs import Count

# Define the test case
def test_count():
    motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
    result = Count(motifs)
    expected = {'A': [1, 2, 1, 0, 0, 2],
                'C': [2, 1, 4, 2, 0, 0],
                'G': [1, 1, 0, 2, 1, 1],
                'T': [1, 1, 0, 1, 4, 2]}
    assert result == expected, f"Expected {expected}, but got {result}"

# Run the test case
if __name__ == "__main__":
    test_count()
    print("Test case passed.")
