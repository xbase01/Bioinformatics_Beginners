import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the function to be tested
from approximate_pattern_count_utils import approximate_pattern_count

# Define the test cases
def test_approximate_pattern_count():
    # Test case 0
    pattern_0 = "GAGG"
    text_0 = "TTTAGAGCCTTCAGAGG"
    d_0 = 2
    result_0 = approximate_pattern_count(pattern_0, text_0, d_0)
    expected_0 = 4
    assert result_0 == expected_0, f"Expected {expected_0}, but got {result_0}"

    # Test case 1
    pattern_1 = "AAAA"
    text_1 = "AACAAGCATAAACATTAAAGAG"
    d_1 = 1
    result_1 = approximate_pattern_count(pattern_1, text_1, d_1)
    expected_1 = 9
    assert result_1 == expected_1, f"Expected {expected_1}, but got {result_1}"

# Run the test cases
if __name__ == "__main__":
    test_approximate_pattern_count()
    print("All test cases passed.")

