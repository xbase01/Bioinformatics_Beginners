import sys
import os

# Adjust the path to include the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from Motifs import GreedyMotifSearchWithPseudocounts

class TestGreedyMotifSearchWithPseudocounts(unittest.TestCase):
        
    def test_greedy_motif_search_with_pseudocounts_case2(self):
        Dna = [
            "GGCGTTCAGGCA",
            "AAGAATCAGTCA",
            "CAAGGAGTTCGC",
            "CACGTCAATCAC",
            "CAATAATATTCG"
        ]
        k = 3
        t = 5
        expected_output = [
            "TTC",
            "ATC",
            "TTC",
            "ATC",
            "TTC"
        ]
        
        result = GreedyMotifSearchWithPseudocounts(Dna, k, t)
        
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()

