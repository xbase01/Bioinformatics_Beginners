import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the function to be tested
from symbol_array_utils import symbol_array

# Define the test cases
def test_symbol_array():
    # Test case 0
    genome_0 = "AAAAGGGG"
    symbol_0 = "A"
    result_0 = symbol_array(genome_0, symbol_0)
    expected_0 = {0: 4, 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    assert result_0 == expected_0, f"Expected {expected_0}, but got {result_0}"

    # Test case 1
    genome_1 = "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"
    symbol_1 = "CC"
    result_1 = symbol_array(genome_1, symbol_1)
    expected_1 = {0: 7, 1: 7, 2: 7, 3: 7, 4: 7, 5: 7, 6: 7, 7: 6, 8: 6, 9: 6, 10: 6, 11: 6, 12: 6, 13: 6, 14: 6, 15: 6, 16: 6, 17: 5, 18: 5, 19: 5, 20: 4, 21: 4, 22: 4, 23: 4, 24: 4, 25: 3, 26: 3, 27: 3, 28: 3, 29: 3, 30: 3, 31: 3, 32: 3, 33: 3, 34: 3, 35: 3, 36: 3, 37: 3, 38: 3, 39: 3, 40: 3, 41: 3, 42: 3, 43: 2, 44: 2, 45: 2, 46: 2, 47: 2, 48: 2, 49: 2, 50: 3, 51: 3, 52: 3, 53: 3, 54: 3, 55: 3, 56: 3, 57: 3, 58: 2, 59: 2, 60: 2, 61: 2, 62: 3, 63: 3, 64: 3, 65: 3, 66: 3, 67: 3, 68: 3, 69: 3, 70: 3, 71: 3, 72: 3, 73: 3, 74: 3, 75: 3, 76: 4, 77: 4, 78: 4, 79: 4, 80: 4, 81: 4, 82: 4, 83: 4, 84: 4, 85: 4, 86: 5, 87: 5, 88: 5, 89: 6, 90: 6, 91: 6, 92: 6, 93: 6, 94: 7, 95: 7, 96: 7, 97: 7, 98: 7, 99: 7, 100: 7, 101: 7, 102: 7, 103: 7, 104: 6, 105: 6, 106: 6, 107: 7, 108: 7, 109: 7, 110: 7, 111: 7, 112: 8, 113: 8, 114: 8, 115: 8, 116: 7, 117: 7, 118: 7, 119: 7, 120: 7, 121: 7, 122: 7, 123: 7, 124: 7, 125: 7, 126: 7, 127: 8, 128: 7, 129: 7, 130: 7, 131: 7, 132: 7, 133: 7, 134: 7}
    assert result_1 == expected_1, f"Expected {expected_1}, but got {result_1}"

# Run the test cases
if __name__ == "__main__":
    test_symbol_array()
    print("All test cases passed.")
