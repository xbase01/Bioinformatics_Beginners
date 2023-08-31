# test/test_count_with_pseudocounts.py

import sys
import os

# Adjust the path to include the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Motifs import CountWithPseudocounts
from motifs_pseudocounts_utils import CountWithPseudocounts as CountWithPseudocountsUtils

def test_count_with_pseudocounts():
    # Sample input
    motifs = ['AACGTA', 'CCCGTT', 'CACCTT', 'GGATTA', 'TTCCGG']
    
    # Expected output
    expected_output = {
        'A': [2, 3, 2, 1, 1, 3],
        'C': [3, 2, 5, 3, 1, 1],
        'G': [2, 2, 1, 3, 2, 2],
        'T': [2, 2, 1, 2, 5, 3]
    }

    # Test the function from Motifs.py
    result = CountWithPseudocounts(motifs)
    assert result == expected_output, f"Motifs.py: Expected {expected_output}, but got {result}"

    # Test the function from motifs_pseudocounts_utils.py
    result_utils = CountWithPseudocountsUtils(motifs)
    assert result_utils == expected_output, f"motifs_pseudocounts_utils.py: Expected {expected_output}, but got {result_utils}"

if __name__ == "__main__":
    test_count_with_pseudocounts()
    print("All tests passed!")

