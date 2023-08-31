from motifs_count_utils import Count  # Import the Count function from motifs_count_utils.py

def Consensus(Motifs):
    """
    Compute the consensus string of a list of motifs.

    Args:
        Motifs (list): List of strings representing motifs.

    Returns:
        str: The consensus string of the motifs.
    """
    k = len(Motifs[0])  # Length of each motif
    count = Count(Motifs)  # Calculate the count matrix using the Count function
    consensus = ""

    for j in range(k):  # Iterate through columns of count matrix
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol  # Add the most frequent symbol to the consensus string

    return consensus

