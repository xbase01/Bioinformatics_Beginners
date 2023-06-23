#!/usr/bin/python3


def FrequencyMap(Text, k):
    """
    Calculate the frequency of each k-mer in the given text.

    Args:
        Text (str): The input text.
        k (int): The length of k-mer.

    Returns:
        dict: A dictionary mapping each k-mer to its frequency.

    """
    freq = {}  # Create an empty dictionary to store the frequencies
    n = len(Text)

    # Iterate over all possible k-mers in the text
    for i in range(n - k + 1):
        Pattern = Text[i:i + k]
        if Pattern in freq:
            freq[Pattern] += 1
        else:
            freq[Pattern] = 1

    return freq


# Example usage

Text = "CGATATATCCATAG"
k = 3
result = FrequencyMap(Text, k)
print(result)
