import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# Download stopwords (only required once)
nltk.download('stopwords')
nltk.download('punkt')
# Sample text (you can replace this with any text input)
text_data = """
Hello! This is an NLP preprocessing example. It includes Filtration, Script
Validation,
and text cleaning. Numbers like 123 and special symbols #@$%^&* should
be removed.
Привет! (This is a Russian word that should be removed if validating
English text.)
"""
# Function to perform text preprocessing
def preprocess_text(text):
# 1. Convert text to lowercase
    text = text.lower()
# 2. Remove special characters, punctuation, and numbers using regex
    text = re.sub(r'[^a-zA-Z\s]', '', text) # Keeps only English alphabets andspaces
# 3. Tokenization
    tokens = word_tokenize(text)
# 4. Remove stopwords (common words like "the", "is", "and" that addlittle meaning)
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word not in stop_words]
# 5. Join words back into a clean text string
    clean_text = " ".join(filtered_tokens)
    return clean_text
# Apply the preprocessing function
processed_text = preprocess_text(text_data)
# Print the results
print("Original Text:\n", text_data)
print("\nPreprocessed Text:\n", processed_text)
