import nltk
import re
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# Download required NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
# Sample text corpus (You can replace this with any text dataset)
corpus = [
"Natural Language Processing is amazing!",
"Bag of Words model is a simple feature extraction method in NLP.",
"Machine learning techniques use Bag of Words for text classification."
]
# Function to preprocess text (lowercasing, removing special characters, andstopwords)
def preprocess_text(text):
 text = text.lower() # Convert to lowercase
 text = re.sub(r'[^a-z\s]', '', text) # Remove special characters andnumbers
 tokens = word_tokenize(text) # Tokenize words
 stop_words = set(stopwords.words("english")) # Get English stopwords
 filtered_tokens = [word for word in tokens if word not in stop_words] #Remove stopwords
 return " ".join(filtered_tokens)
# Preprocess each document in the corpus
clean_corpus = [preprocess_text(doc) for doc in corpus]
# Initialize CountVectorizer (Bag of Words model)
vectorizer = CountVectorizer()
# Fit and transform the clean corpus to build the BoW representation
X = vectorizer.fit_transform(clean_corpus)
# Convert the BoW matrix to a DataFrame for better visualization
bow_df = pd.DataFrame(X.toarray(),
columns=vectorizer.get_feature_names_out())
# Print Results
print("\nCleaned Corpus:\n", clean_corpus)
print("\nBag of Words Representation:\n", bow_df)
