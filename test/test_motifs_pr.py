import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the function to be tested
from motifs_pr_utils import Pr

# Define the test case
def test_pr():
    text = "ACGGGGATTACC"
    profile = {
        'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
        'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
        'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
        'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
    }
    
    result = Pr(text, profile)
    expected = 0.0008398080000000002
    assert result == expected, f"Expected {expected}, but got {result}"

# Run the test case
if __name__ == "__main__":
    test_pr()
    print("Test case passed.")

