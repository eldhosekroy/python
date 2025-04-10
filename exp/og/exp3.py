import nltk
from nltk.probability import FreqDist
# Sample text (You can replace this with any text input)
text_data = """
The network is a system of computers that are connected to share data.
The communication within the network is essential for smooth operations.
"""
# Tokenizing the text (splitting it into words)
tokens = nltk.word_tokenize(text_data.lower()) # Convert to lowercase to ensure uniformity
# Task 1: Count the total number of words (tokens)
total_tokens = len(tokens)
print(f"1. Total number of words (tokens): {total_tokens}")
# Task 2: Count the total number of unique words (types)
unique_words = len(set(tokens)) # Using set() to get unique words
print(f"2. Total number of unique words (types): {unique_words}")
# Task 3: Count how many times the word "the" appears
freq_dist = FreqDist(tokens) # Creating a frequency distribution of words
the_count = freq_dist["the"] # Count occurrences of "the"
print(f"3. Number of times the word 'the' appears: {the_count}")
# Task 4: Calculate percentage of "the" in the entire text
the_percentage = (the_count / total_tokens) * 100
print(f"4. Percentage of 'the' in the text: {the_percentage:.2f}%")
