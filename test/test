import sys
import os
import unittest

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the function to be tested
from skew_array_utils import skew_array

class TestSkewArray(unittest.TestCase):

    def test_skew_array_sample(self):
        genome = "CATGGGCATCGGCCATACGCC"
        expected_output = [0, -1, -1, -1, 0, 1, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, -1, 0, -1, -2]
        self.assertEqual(skew_array(genome), expected_output)

    # Add more test cases here if needed

if __name__ == "__main__":
    unittest.main()

