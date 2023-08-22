from skew_array_utils import skew_array

def minimum_skew(Genome):
    """
    Find position(s) in a genome where the skew diagram attains a minimum.
    
    Args:
        Genome (str): A DNA string.
    
    Returns:
        list: List of integer(s) i minimizing Skew[i] for Genome.
    """
    positions = []  # Initialize an empty list to store positions
    skew_values = skew_array(Genome)  # Calculate the skew array
    
    min_skew = min(skew_values)  # Find the minimum value in the skew array
    
    # Iterate over the range of the skew array length
    for i in range(len(skew_values)):
        if skew_values[i] == min_skew:
            positions.append(i)  # Append positions achieving the minimum skew
    
    return positions
