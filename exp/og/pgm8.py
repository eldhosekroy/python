from nltk.metrics import edit_distance, jaccard_distance
# Step 2: Define the Strings
text1 = "kitten"
text2 = "sitting"
# Step 3: Calculate Edit Distance
edit_dist = edit_distance(text1, text2)
# Step 4: Calculate Jaccard Distance
jaccard_dist = jaccard_distance(set(text1), set(text2))
# Step 5: Print Results
print("Edit Distance:", edit_dist)
print("Jaccard Distance:", jaccard_dist)
