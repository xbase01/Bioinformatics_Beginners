import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the function to be tested
from motifs_ProfileMostProbableKmer_utils import ProfileMostProbableKmer

def test_profile_most_probable_pattern():
    # Test case 0
    text_0 = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
    k_0 = 5
    profile_0 = {
        'A': [0.2, 0.2, 0.3, 0.2, 0.3],
        'C': [0.4, 0.3, 0.1, 0.5, 0.1],
        'G': [0.3, 0.3, 0.5, 0.2, 0.4],
        'T': [0.1, 0.2, 0.1, 0.1, 0.2]
    }
    result_0 = ProfileMostProbableKmer(text_0, k_0, profile_0)
    expected_0 = "CCGAG"
    assert result_0 == expected_0, f"Expected {expected_0}, but got {result_0}"

    # Add more test cases here...

# Run the test cases
if __name__ == "__main__":
    test_profile_most_probable_pattern()
    print("All test cases passed.")

