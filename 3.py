# Function to compute the number of characters, words, and lines in a file
def compute_file_statistics(input):
    with open(file_name, "r") as infile:  # Open the file in read mode
        lines = infile.readlines()  # Read all lines from the file

        # Count the number of lines
        num_lines = len(lines)

        # Count the number of words (split each line and count words)
        num_words = sum(len(line.split()) for line in lines)

        # Count the number of characters (sum length of each line)
        num_characters = sum(len(line) for line in lines)

    return num_lines, num_words, num_characters


# Specify the file name
file_name = "input4.1.txt"  # Change this to the path of your file

# Compute statistics
lines, words, characters = compute_file_statistics(input)

# Print the results
print(f"Number of lines: {lines}")
print(f"Number of words: {words}")
print(f"Number of characters: {characters}")