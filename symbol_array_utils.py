from patternCount import PatternCount

def symbol_array(Genome, symbol):
    """
    Calculate the symbol array of a given Genome with respect to a specific symbol.

    Args:
        Genome (str): The input genome sequence.
        symbol (str): The specific symbol to calculate the symbol array for.

    Returns:
        dict: A dictionary containing the symbol array where keys are positions and values are symbol occurrences.

    """
    array = {}  # Initialize an empty dictionary to store the symbol array
    n = len(Genome)  # Get the length of the Genome sequence
    ExtendedGenome = Genome + Genome[0:n//2]  # Create an extended Genome sequence by appending the first half

    # Iterate through each position in the Genome
    for i in range(n):
        # Calculate the occurrences of the symbol in the current window of ExtendedGenome
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])

    return array
