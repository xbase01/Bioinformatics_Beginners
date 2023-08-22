# Replication.py

def Reverse(Pattern):
    """
    Reverse the given DNA sequence pattern.

    Args:
        Pattern (str): The DNA sequence pattern.

    Returns:
        str: The reversed pattern.

    """
    reverse_pattern = ""
    for char in Pattern:
        reverse_pattern = char + reverse_pattern
    return reverse_pattern


def Complement(Pattern):
    """
    Compute the complement of a DNA sequence pattern.

    Args:
        Pattern (str): The DNA sequence pattern.

    Returns:
        str: The complement of the pattern.

    """
    complement = ""
    for nucleotide in Pattern:
        if nucleotide == 'A':
            complement += 'T'
        elif nucleotide == 'T':
            complement += 'A'
        elif nucleotide == 'C':
            complement += 'G'
        elif nucleotide == 'G':
            complement += 'C'
    return complement


def ReverseComplement(Pattern):
    """
    Compute the reverse complement of a DNA sequence pattern.

    Args:
        Pattern (str): The DNA sequence pattern.

    Returns:
        str: The reverse complement of the pattern.

    """
    reversed_pattern = Reverse(Pattern)
    reverse_complement = Complement(reversed_pattern)
    return reverse_complement


def PatternCount(Pattern, Text):
    """
    Count the number of occurrences of a pattern in a given text.

    Args:
        Pattern (str): The pattern to count.
        Text (str): The text to search for the pattern.

    Returns:
        int: The count of occurrences of the pattern.

    """
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count


def FrequencyMap(Text, k):
    """
    Create a frequency map of k-mers in the given text.

    Args:
        Text (str): The input text.
        k (int): The length of k-mers.

    Returns:
        dict: A dictionary with k-mers as keys and their frequencies as values.

    """
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        kmer = Text[i:i+k]
        if kmer in freq:
            freq[kmer] += 1
        else:
            freq[kmer] = 1
    return freq


def FrequentWords(Text, k):
    """
    Find the most frequent k-mers in the given text.

    Args:
        Text (str): The input text.
        k (int): The length of k-mers.

    Returns:
        list: A list of the most frequent k-mers.

    """
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words


def PatternMatching(Pattern, Genome):
    """
    Find all starting positions of a pattern in a genome.

    Args:
        Pattern (str): The pattern to search for.
        Genome (str): The genome to search in.

    Returns:
        list: A list of starting positions of the pattern in the genome.

    """
    positions = []
    n = len(Genome)
    for i in range(n - len(Pattern) + 1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions


def SymbolArray(Genome, symbol):
    """
    Create a symbol array for a given symbol in a genome.

    Args:
        Genome (str): The input genome.
        symbol (str): The symbol to count.

    Returns:
        dict: A dictionary with indices as keys and symbol counts as values.

    """
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i] - 1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i] + 1
    return array


def SkewArray(Genome):
    """
    Calculate the skew array for a given genome.

    Args:
        Genome (str): The input genome.

    Returns:
        list: A list of skew values at each position.

    """
    skew = [0]
    n = len(Genome)
    for i in range(n):
        if Genome[i] == 'C':
            skew.append(skew[i] - 1)
        elif Genome[i] == 'G':
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
    return skew


def MinimumSkew(Genome):
    """
    Find position(s) in a genome where the skew diagram attains a minimum.

    Args:
        Genome (str): A DNA string.

    Returns:
        list: List of integer(s) i minimizing Skew[i] for Genome.
    """
    positions = [] # Initialize an empty list to store positions
    skew_values = SkewArray(Genome) #Calculate the skew array

    min_skew = min(skew_values) 

    for i in range(len(skew_values)):
        if skew_values[i] == min_skew:
            positions.append(i)

    return positions

def HammingDistance(p, q):
    """
    Compute the Hamming distance between two strings.

    Args:
        p (str): First string.
        q (str): Second string.

    Returns:
        int: The Hamming distance between the two strings.
    """
    if len(p) != len(q):
        rasie ValueError("Input strings must be of equal length")

    hamming_distance = sum(1 for i in range(len(p)) if p[i] != q[i])
    return hamming_distance


def ApproximatePatternMatching(Text, Pattern, d):
    """
    Finds all approximate occurrences of a pattern in a string.

    Args:
        Pattern (str): The pattern to search for.
        Text (str): The text in which to search.
        d (int): The maximum allowed number of mismatches.

    Returns:
        list: A list of starting positions where Pattern appears as a substring.
    """
    positions = []
    k = len(Pattern)
    for i in range(len(Text) - k + 1):
        substring = Text[i:i+k]
        if HammingDistance(Pattern, substring) <= d:
            positions.append(i)
    return positions


def ApproximatePatternCount(Pattern, Text, d):
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
# You can add more functions or code here if needed

