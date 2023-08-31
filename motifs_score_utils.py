from motifs_consensus_utils import Consensus

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
