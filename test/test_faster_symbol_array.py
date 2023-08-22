import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from faster_symbol_array_utils import faster_symbol_array

def test_faster_symbol_array():
    # Specify the path to the E_coli.txt file in the parent directory
    e_coli_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'E_coli.txt')
    
    # Read the content of the E_coli.txt file
    with open(e_coli_path, 'r') as file:
        genome = file.read().strip()

    symbol = 'A'
    result = faster_symbol_array(genome, symbol)

    # Print the result for testing
    print(result)

if __name__ == "__main__":
    test_faster_symbol_array()
