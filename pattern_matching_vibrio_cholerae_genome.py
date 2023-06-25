def PatternMatching(Pattern, Genome):
    """
    Find all starting positions of a pattern in a genome.

    Args:
        Pattern (str): The pattern to search for.
        Genome (str): The genome sequence.

    Returns:
        list: A list of starting positions of the pattern in the genome.

    """
    positions = []  # output variable
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

# Read the genome from the file "Vibrio_cholerae.txt.
with open("Vibrio_cholerae.txt", "r") as file:
    v_cholerae = file.read().strip()

# Call PatternMatching
Pattern = "CTTGATCAT"
Genome = v_cholerae
positions = PatternMatching(Pattern, Genome)
print(positions)
