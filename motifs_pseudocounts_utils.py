def CountWithPseudocounts(Motifs):
    """
    Generate the count matrix with pseudocounts from a list of motifs.

    Args:
        Motifs (list): A list of DNA motifs (strings).

    Returns:
        dict: The count matrix with pseudocounts where keys are nucleotide symbols ('A', 'C', 'G', 'T')
              and values are lists representing the occurrences of symbols at each position.
    """
    count = {}  # Initialize the count matrix as a dictionary
    k = len(Motifs[0])  # Length of each motif

    # Create an empty list for each nucleotide symbol
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)  # Add pseudocount of 1 for each position j

    t = len(Motifs)  # Total number of motifs
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count  # Return the generated count matrix with pseudocounts

