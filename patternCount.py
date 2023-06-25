def PatternCount(Pattern, Text):
    """
    Function that counts number of times a pattern occurs in a DNA sequence.

    Args:
        Pattern (str): Pattern to be counted.
        Text (str): Sequence where pattern will be checked and counted.

    Returns:
        int: Number of occurrences of the pattern in the sequence.

    """
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count


# Read the genome from the file "Vibrio_cholerae.txt.
with open("Vibrio_cholerae.txt", "r") as file:
        Text = file.read().strip()  # Define the Text sequence


# Count the occurrences of pattern.

Pattern_1 = "ATGATCAAG"
count_1 = PatternCount(Pattern_1, Text)

Pattern_2 = "CTTGATCAT"
count_2 = PatternCount(Pattern_2, Text)

# Calculate the sum of counts
total_count = count_1 + count_2

# Print the sum
print(total_count)
