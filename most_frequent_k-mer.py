#!/usr/bin/python3

from frequency_kmer import FrequencyMap

def FrequentWords(Text, k):
    """
    Find the most frequent k-mers in the given text.

    Args:
        Text (str): The input text.
        k (int): The length of k-mer.

    Returns:
        List: A list of the most frequent k-mers.

    """
    words = [] # Create an empty list to store the most frequent k-mers
    freq = FrequencyMap(Text, k) # Calculate the frequency of each k-mer
    m = max(freq.values()) # Find the maximum frequency among the k-mers

    # Iterate over each k-mer, check if its frequency matches max freqency
    for key in freq:
        if freq[key] == m:
            words.append(key)  # Add the k-mer to the list of most frequent k-mers

    return words

# Example usage
Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
result = FrequentWords(Text, k)
print(result)
