from hamming_distance_utils import HammingDistance


def approximate_pattern_matching(Pattern, Text, d):
    """
    Finds all approximate occurrences of a pattern in a string.

    Args:
        Pattern (str): The pattern to search for.
        Text (str): The text in which to search.
        d (int): The maximum allowed number of mismatches.

    Returns:
        list: A list of starting positions where Pattern appears as a substring of Text with at most d mismatches.
    """
    positions = []
    k = len(Pattern)
    for i in range(len(Text) - k + 1):
        substring = Text[i:i+k]
        if HammingDistance(Pattern, substring) <= d:
            positions.append(i)
    return positions
