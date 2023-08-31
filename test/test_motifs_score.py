import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the function to be tested
from motifs_score_utils import Score

def test_score():
    motifs = [
        "AACGTA",
        "CCCGTT",
        "CACCTT",
        "GGATTA",
        "TTCCGG"
    ]
    result = Score(motifs)
    expected = 14
    assert result == expected, f"Expected {expected}, but got {result}"

# Run the test cases
if __name__ == "__main__":
    test_score()
    print("All test cases passed.")

