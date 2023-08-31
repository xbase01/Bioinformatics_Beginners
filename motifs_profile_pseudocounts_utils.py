from motifs_pseudocounts_utils import CountWithPseudocounts


def ProfileWithPseudocounts(Motifs):
    """
    Calculate the profile matrix for a list of DNA motifs with pseudocounts.

    Args:
        Motifs (list): A list of DNA motifs represented as strings.

    Returns:
        dict: A dictionary representing the profile matrix with pseudocounts, where keys are nucleotides
            ('A', 'C', 'G', 'T') and values are lists of probabilities for each purpose.
    """
    t = len(Motifs) # Number of motifs
    k = len(Motifs[0]) # Length of each motif
    profile = {} # Initialize the profile matrix
    
    count_matrix = CountWithPseudocounts(Motifs) # Calculate the count matrix with pseudocounts using the CountWithPseudocounts function.

    # Iterate over each nucleotide ('A', 'C', 'G', 'T')
    for symbol in "ACGT":
        profile[symbol] = [] # Initialize the list for this symbol
        # Iterate over each position j in the motifs
        for j in range(k):
            frequency = count_matrix[symbol][j] / (t + 4) # Divide count by the number of motifs plus pseudocounts
            profile[symbol].append(frequency) # Add the frequency to the profile

    return profile

