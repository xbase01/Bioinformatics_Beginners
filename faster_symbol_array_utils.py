from faster_pattern_count_utils import faster_pattern_count

def faster_symbol_array(Genome, symbol):
    """
    Compute the symbol array of a given Genome corresponding to a specific symbol.

    This algorithm efficiently computes the symbol array by utilizing a sliding window approach
    and tracking the difference in counts between consecutive positions.

    Args:
        Genome (str): The input genome sequence.
        symbol (str): The symbol for which the symbol array needs to be computed.

    Returns:
        dict: A dictionary containing the symbol array values for each position in the Genome.

    """
    array = {}  # Initialize the dictionary to store symbol array values
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # Compute the symbol count for the first half of the genome
    array[0] = faster_pattern_count(symbol, Genome[0:n//2])

    # Iterate over the positions in the genome
    for i in range(1, n):
        # Initialize the current array value as the previous array value
        array[i] = array[i-1]

        # Update the array value based on the current position's symbol
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i] - 1  # Decrease count if previous symbol matches
        if ExtendedGenome[i + (n//2) - 1] == symbol:
            array[i] = array[i] + 1  # Increase count if current symbol matches

    return array
