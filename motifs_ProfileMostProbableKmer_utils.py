from motifs_pr_utils import Pr

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
        if probability > max_probability:
            max_probability = probability
            most_probable_kmer = kmer

    return most_probable_kmer

