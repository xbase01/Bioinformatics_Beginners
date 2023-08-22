# Input:  A String Genome
# Output: The skew array of Genome as a list.
def skew_array(Genome):
    # your code here
    """
    Calculate the skew array of a DNA sequence Genome.

    Args:
        Genome (str): The DNA sequence.

    Returns:
        list: A list containing the skew values for each position in the Genome.

    """
    skew = [0]  # Initialize the skew array with the first element as 0
    count = 0   # Initialize the count of G - C

    for nucleotide in Genome:
        if nucleotide == 'G':
            count += 1
        elif nucleotide == 'C':
            count -= 1
        skew.append(count)  # Append the current skew value to the list

    return skew
