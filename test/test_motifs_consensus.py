import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the function to be tested
from motifs_consensus_utils import Consensus

# Define the test case
def test_consensus():
    motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
    result = Consensus(motifs)
    expected = "CACCTA"
    assert result == expected, f"Expected {expected}, but got {result}"

# Run the test case
if __name__ == "__main__":
    test_consensus()
    print("Test case passed.")

