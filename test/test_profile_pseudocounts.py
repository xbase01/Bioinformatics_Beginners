# test/test_count_with_pseudocounts.py

import sys
import os

# Adjust the path to include the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# motifs_profile_pseudocounts_utils.py

import unittest
from Motifs import ProfileWithPseudocounts

class TestProfileWithPseudocounts(unittest.TestCase):

    def test_profile_with_pseudocounts(self):
        Motifs = [
            "AACGTA",
            "CCCGTT",
            "CACCTT",
            "GGATTA",
            "TTCCGG"
        ]
        expected_output = {
            'A': [0.2222222222222222, 0.3333333333333333, 0.2222222222222222, 0.1111111111111111, 0.1111111111111111, 0.3333333333333333],
            'C': [0.3333333333333333, 0.2222222222222222, 0.5555555555555556, 0.3333333333333333, 0.1111111111111111, 0.1111111111111111],
            'G': [0.2222222222222222, 0.2222222222222222, 0.1111111111111111, 0.3333333333333333, 0.2222222222222222, 0.2222222222222222],
            'T': [0.2222222222222222, 0.2222222222222222, 0.1111111111111111, 0.2222222222222222, 0.5555555555555556, 0.3333333333333333]
        }

        result = ProfileWithPseudocounts(Motifs)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

