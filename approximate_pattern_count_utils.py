from hamming_distance_utils import HammingDistance

# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def approximate_pattern_count(Pattern, Text, d):
    # your code here
    """
    Compute the number of occurrences of Pattern in Text with at most d mismatches.

    Args:
        Pattern (str): Pattern to be matched.
        Text (str): Text in which pattern will be searched.
        d (int): Maximum allowed mismatches.

    Returns:
        int: Number of occurrences of Pattern with at most d mismatches.
    """
    count = 0
    k = len(Pattern)
    n = len(Text)
    for i in range(n - k + 1):
        substring = Text[i:i+k]
        if HammingDistance(Pattern, substring) <= d:
            count += 1
    return count
