def PatternCount(Pattern, Text):
    """
    Function that counts number of times a pattern occurs in a DNA sequence.

    Args:
        Pattern (str): Pattern to be counted.
        Text (str): Sequence where pattern will be checked and counted.

    Returns:
        int: Number of occurrences of the pattern in the sequence.

    """
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count
