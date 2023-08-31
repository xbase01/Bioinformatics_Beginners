import sys
import os


# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the function to be tested
from motifs_profile_utils import Profile

# Define the test cases
def test_profile():
    # Test case 0
    motifs_0 = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
    result_0 = Profile(motifs_0)
    expected_0 = {
        'A': [0.2, 0.4, 0.2, 0.0, 0.0, 0.4],
        'C': [0.4, 0.2, 0.8, 0.4, 0.0, 0.0],
        'G': [0.2, 0.2, 0.0, 0.4, 0.2, 0.2],
        'T': [0.2, 0.2, 0.0, 0.2, 0.8, 0.4]
    }
    assert result_0 == expected_0, f"Expected {expected_0}, but got {result_0}"

# Run the test cases
if __name__ == "__main__":
    test_profile()
    print("All test cases passed.")

