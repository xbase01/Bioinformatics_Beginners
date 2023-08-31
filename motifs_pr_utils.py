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

