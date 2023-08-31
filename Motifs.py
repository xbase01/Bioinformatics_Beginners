def Count(Motifs):
    """
    Generate the count matrix from a list of motifs.

    Args:
        Motifs (list): A list of DNA motifs (strings).

    Returns:
        dict: The count matrix where keys are nucleotide symbols ('A', 'C', 'G', 'T')
              and values are lists representing the occurrences of symbols at each position.
    """
    count = {}  # Initialize the count matrix as a dictionary
    k = len(Motifs[0])  # Length of each motif

    # Create an empty list for each nucleotide symbol
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)  # Append 0 for each position j

    t = len(Motifs)  # Total number of motifs
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count  # Return the generated count matrix

def Profile(Motifs):
    """
    Calculate the profile matrix for a list of DNA motifs.

    Args:
        Motifs (list): A list of DNA motifs represented as strings.

    Returns:
        dict: A dictionary representing the profile matrix, where keys are nucleotides
            ('A', 'C', 'G', 'T') and values are lists of probabilities for each purpose.
    """
    t = len(Motifs) # Number of motifs
    k = len(Motifs[0]) # Length of each motif
    profile = {} # Initialize the profile matrix

    count_matrix = Count(Motifs) # Calculate the count matrix using the Count function.

    # Iterate over each nucleotide ('A', 'C', 'G', 'T')
    for symbol in "ACGT":
        profile[symbol] = [] # Initialize the list for this symbol
        # Iterate over each position j in the motifs
        for j in range(k):
            frequency = count_matrix[symbol][j] / t # Divide count by the number of motifs
            profile[symbol].append(frequency) # Add the frequency to the profile

    return profile


def Consensus(Motifs):
    """
    Compute the consensus string of a list of motifs.

    Args:
        Motifs (list): List of strings representing motifs.

    Returns:
        str: The consensus string of the motifs.
    """
    k = len(Motifs[0])  #Length of each motif
    count = Count(Motifs) # Calculate the count matrix using the Count function.
    consensus = ""

    for j in range(k): # Iterate through columns of count matrix
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            m = count[symbol][j]
            frequentSymbol = symbol
        consensus += frequentSymbol  # Add the most frequent symbol to the consensus string.

    return consensus

def Score(Motifs):
    """
    Calculate the score of a list of motifs based on their distance from the consensus string.

    Args:
        Motifs (list): List of DNA motifs.

    Returns:
        int: Score of the motifs.
    """
    consensus = Consensus(Motifs) # Calculate the consensus string using the consensus function.
    k = len(consensus)
    score = 0

    for i in range(k):
        mismatch_count = sum(1 for motif in Motifs if motif[i] != consensus[i])
        score += mismatch_count

    return score


def Pr(Text, Profile):
    """
    Calculate the probability of observing a given Text string according to the provided Profile matrix.

    Args:
        Text (str): The input DNA sequence.
        Profile (dict): The profile matrix.

    Returns:
        float: The probability of observing the given Text according to the Profile matrix.
    """
    p = 1
    k = len(Text)

    for i in range(k):
        p *= Profile[Text[i]][i]

    return p

def ProfileMostProbableKmer(Text, k, Profile):
    """
    Find a Profile-most probable k-mer in a given text.

    Args:
        Text (str): The input DNA string.
        k (int): The length of the k-mer.
        Profile (dict): The profile matrix as a dictionary of lists.

    Returns:
        str: A Profile-most probable k-mer in Text.
    """
    max_probability = -1
    most_probable_kmer = ""

    for i in range(len(Text) - k + 1):
        kmer = Text[i:i+k]
        probability = Pr(kmer, Profile)
        A
        if probability > max_probability:
            max_probability = probability
            most_probable_kmer = kmer

    return most_probable_kmer


def CountWithPseudocounts(Motifs):
    """
    Generate the count matrix with pseudocounts from a list of motifs.

    Args:
        Motifs (list): A list of DNA motifs (strings).

    Returns:
        dict: The count matrix with pseudocounts where keys are nucleotide symbols ('A', 'C', 'G' 'T')
              and values are lists representing the occurrences of symbols at each position.
    """
    count = {} # Initialize the count matrix as a dictionary
    k = len(Motifs[0]) # Length of each motif

    # Create an empty list for each nucleotide symbol
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1) # Add pseudocount of 1 for each position j

    t = len(Motifs) # Total number of motifs
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count # Return the generated count matrix with pseudocounts


def ProfileWithPseudocounts(Motifs):
    """
    Calculate the profile matrix for a list of DNA motifs with pseudocounts.

    Args:
        Motifs (list): A list of DNA motifs represented as strings.

    Returns:
        dict: A dictionary representing the profile matrix with pseudocounts, where keys are nucleotides
              ('A', 'C', 'G', 'T') and values are lists of probabilities for each purpose.
    """
    t = len(Motifs) # Number of motifs
    k = len(Motifs[0]) # Length of each motif
    profile = {} # Initialize the profile matrix

    # Calculate the count matrix with pseudocounts using the CountWithPseudocounts function.
    count_matrix = CountWithPseudocounts(Motifs)

    # Iterate over each nucleotide ('A', 'C', 'G', 'T')
    for symbol in "ACGT":
        profile[symbol] = []  #Initialize the list for this symbol
        # Iterate over each position j in the motifs
        for j in range(k):
            frequency = count_matrix[symbol][j] / (t + 4) # Divide count by number of motifs plus pseudocounts
            profile[symbol].append(frequency) # Add the frequency to the profile.

    return profile

def ScoreWithPseudocounts(Motifs):
    """
    Calculate the score of a list of motifs based on pseudocounts.

    Args:
        Motifs (list): List of DNA motifs.

    Returns:
        int: Score of the motifs.
    """
    count = CountWithPseudocounts(Motifs)
    score = 0
    for j in range(len(Motifs[0])):
        max_count = max(count[symbol][j] for symbol in "ACGT")
        score += sum(count[symbol][j] for symbol in "ACGT") - max_count
    return score

def ProfileMostProbablePattern(Text, k, profile):
    max_prob = -1
    most_probable = ""
    for i in range(len(Text) - k + 1):
        pattern = Text[i:i+k]
        prob = 1
        for j in range(k):
            prob *= profile[pattern[j]][j]
        if prob > max_prob:
            max_prob = prob
            most_probable = pattern
    return most_probable

def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    """
    GreedyMotifSearch algorithm for finding the best-scoring motifs in a list of Dna strings with pseudocounts.

    Args:
        Dna (list): A list of DNA strings.
        k (int): The length of motifs to search for.
        t (int): The number of DNA strings in Dna.

    Returns:
        list: A list of best-scoring motifs found.
    """

    BestMostifs = [string[:k] for string in Dna]

    for i in range(len(Dna[0]) - k + 1):
        Motifs = [Dna[0][i:i+k]]

        for j in range(1, t):
            profile = ProfileWithPseudocounts(Motifs[0:j]) # Generate profile matrix with psedocounts
            motif = ProfileMostProbablePattern(Dna[j], k, profile)
            Motifs.append(motif)

        if ScoreWithPseudocounts(Motifs) < ScoreWithPseudocounts(BestMotifs):
            BestMotifs = Motifs

    return BestMotifs

def Motifs(Profile, Dna):
    """
    Find the Profile-most probable k-mers in a list of DNA sequences based on the provided profile matrix.

    Args:
        Profile (dict): The profile matrix as a dictionary of lists.
        Dna (list): A list of DNA sequences.

    Returns:
        list: A list of Profile-most probable k-mers, one for each DNA sequence in Dna.
    """
    k = len(Profile['A'])
    most_probable_kmers = []

    for text in Dna:
        most_probable_kmer = ProfileMostProbablePattern(text, k, Profile)
        most_probable_kmers.append(most_probable_kmer)

    return most_probable_kmers

# Random Motifs

import random

def RandomMotifs(Dna, k, t):
    """
    Generate a list of random k-mers from a list of DNA strings.

    Args:
        Dna (list): A list of DNA strings.
        k (int): The length of k-mers to be generated.
        t (int): The number of strings in Dna.

    Returns:
        list: A list of random k-mers, one from each string in Dna.
    """
    random_motifs = []
    for i in range(t):
        start = random.randint(0, len(Dna[i]) - k) # Generate a random startint index
        random_motif = Dna[i][start:start + k] # Extract the random k-mer
        random_motifs.append(random_motif)
    
    return random_motifs

def RandomizedMotifSearch(Dna, k, t):
    """
    Perform the Randomized Motif Search algorithm to fin the best-scoring motifs in a list of DNA strings.

    Args:
        Dna (list): A list of DNA strings.
        k (int): The length of motifs to search for.
        t (int): The number of DNA strings in Dna.

    Returns:
        list: A list of best-scoring motifs found.
    """
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M

    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs

def Normalize(Probabilities):
    """
    Normalize a dictionary of probabilities.

    Args:
        Probabilities (dict): A dictionary where keys are k-mers and values are their probabilities.

    Returns:
        dict: A normalized dictionary where the probability of each k-mer is divided by the sum of all probabilities.
    """
    total_sum = sum(Probabilities.values())
    normalized_probs = {kmer: prob / total_sum for kmer, prob in Probabilities.items()}
    return normalized_probs

def WeightedDie(Probabilities):
    """
    Choose a k-mer randomly with respect to the given probabilities.

    Args:
        Probabilities (dict): A dictionary where keys are k-mers and values are their probabilities.

    Returns:
        str: A randomly chosen k-mer with respect to the probabilities.
    """
    p = random.uniform(0, 1)
    total = 0
    for kmer, prob in Probabilities.items():
        total += prob
        if p < total:
            return kmer

def ProfileGeneratedString(Text, profile, k):
    """
    Generate a k-mer randomly from Text based on a profile matrix.

    Args:
        Test (str): The input DNA string.
        profile (dict): The profile matrix as a dictionary.
        k (int): The length of the k-mer.

    Returns:
        str: A randomly generated k-mer from Text based on the profile matrix.
    """
    n = len(Text)
    probabilities = {}

    for i in range(0, n - k + 1):
        probabilities[Text[i:i + k]] = Pr(Text[i:i + k], profile)

    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

