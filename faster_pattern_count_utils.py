def faster_pattern_count(Pattern, Text):
    """
    Count the number of occurrences of a pattern in a given text using a sliding window approach.

    Args:
        Pattern (str): Pattern to be counted.
        Text (str): Sequence where the pattern will be checked and counted.

    Returns:
        int: Number of occurrences of the pattern in the text.

    """
    pattern_len = len(Pattern)
    text_len = len(Text)
    count = 0

    # Iterate over the text with a sliding window of length pattern_len
    for i in range(text_len - pattern_len + 1):
        window = Text[i:i + pattern_len]
        if window == Pattern:
            count += 1

    return count
