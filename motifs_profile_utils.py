from motifs_count_utils import Count

def Profile(Motifs):
    """
    Calculate the profile matrix for a list of DNA motifs.
    
    Args:
        Motifs (list): A list of DNA motifs represented as strings.
        
    Returns:
        dict: A dictionary representing the profile matrix, where keys are nucleotides
              ('A', 'C', 'G', 'T') and values are lists of probabilities for each position.
    """
    t = len(Motifs)  # Number of motifs
    k = len(Motifs[0])  # Length of each motif
    profile = {}  # Initialize the profile matrix
    
    count_matrix = Count(Motifs)  # Calculate the count matrix using the Count function
    
    # Iterate over each nucleotide ('A', 'C', 'G', 'T')
    for symbol in "ACGT":
        profile[symbol] = []  # Initialize the list for this symbol
        # Iterate over each position j in the motifs
        for j in range(k):
            frequency = count_matrix[symbol][j] / t  # Divide count by the number of motifs
            profile[symbol].append(frequency)  # Add the frequency to the profile
    
    return profile

