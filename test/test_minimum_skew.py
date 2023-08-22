import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the function to be tested
from minimum_skew_utils import minimum_skew

# Define the test cases
def test_minimum_skew():
    # Test case 0
    genome_0 = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
    result_0 = minimum_skew(genome_0)
    expected_0 = [11, 24]
    assert result_0 == expected_0, f"Expected {expected_0}, but got {result_0}"

    #Test case 1
    # Specify the path to the E_coli.txt file in the parent directory
    e_coli_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'E_coli.txt')

    # Read the content of the E_coli.txt file
    with open(e_coli_path, 'r') as file:
        genome_1 = file.read().strip()
    result_1 = minimum_skew(genome_1)
    expected_1 = [3923620]
    assert set(result_1) == set(expected_1), f"Expected {expected_1}, but got {result_1}"


# Run the test cases
if __name__ == "__main__":
    test_minimum_skew()
    print("All test cases passed.")
