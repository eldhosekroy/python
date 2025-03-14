from nltk.corpus import stopwords
# Step 2: Load Stopwords
stop_words = set(stopwords.words('english'))
# Step 3: Define Tokens
tokens = ["NLTK", "is", "a", "powerful", "library", "for", "natural", "language",
"processing", "."]
# Step 4: Remove Stopwords
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
# Step 5: Print Results
print("Filtered Tokens:", filtered_tokens)
