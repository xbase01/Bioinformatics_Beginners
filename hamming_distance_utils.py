# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    # your code here
    """
    Compute the Hamming distance between two strings.

    Args:
        p (str): First string.
        q (str): Second string.

    Returns:
        int: The Hamming distance between the two strings.
    """
    if len(p) != len(q):
        raise ValueError("Input strings must be of equal length")
    
    hamming_distance = sum(1 for i in range(len(p)) if p[i] != q[i])
    return hamming_distance
