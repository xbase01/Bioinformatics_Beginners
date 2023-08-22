import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the function to be tested
from approximate_pattern_matching_utils import approximate_pattern_matching

# Define the test cases
def test_approximate_pattern_matching():
    # Test case 0
    pattern_0 = "GAGG"
    text_0 = "TTTAGAGCCTTCAGAGG"
    d_0 = 2
    result_0 = approximate_pattern_matching(pattern_0, text_0, d_0)
    expected_0 = [2, 4, 11, 13]
    assert result_0 == expected_0, f"Expected {expected_0}, but got {result_0}"

    # Test case 1
    pattern_1 = "ATTCTGGA"
    text_1 = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
    d_1 = 3
    result_1 = approximate_pattern_matching(pattern_1, text_1, d_1)
    expected_1 = [6, 7, 26, 27]
    assert result_1 == expected_1, f"Expected {expected_1}, but got {result_1}"

# Run the test cases
if __name__ == "__main__":
    test_approximate_pattern_matching()
    print("All test cases passed.")

