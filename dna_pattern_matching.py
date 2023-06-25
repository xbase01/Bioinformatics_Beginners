# Write a function PatternMatching that solves the Pattern Matching Problem.

def PatternMatching(pattern, genome):
    """
    Find all starting positions of a pattern in a genome.

    Args:
        pattern (str): The pattern to search for.
        genome (str): The genome sequence.

    Returns:
        list: A list of starting positions of the pattern in the genome.

    """
    positions = []  # Create an empty list to store the starting positions.

    # Iterate over the genome with a char length equal to the pattern length.
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i:i+len(pattern)] == pattern:

            # Append the starting position if it matches pattern.
            positions.append(i)
    return positions
