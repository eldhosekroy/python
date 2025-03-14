import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
# Download stopwords (if not downloaded already)
#nltk.download('stopwords')
#nltk.download('punkt')
from nltk.corpus import stopwords
# Function to preprocess the text (lowercasing, removing punctuation, andstopwords)
def preprocess_text(text):
# Convert to lowercase
 text = text.lower()
# Remove punctuation
 text = text.translate(str.maketrans('', '', string.punctuation))
# Tokenize and remove stopwords
 tokens = nltk.word_tokenize(text)
 stop_words = set(stopwords.words('english'))
 filtered_tokens = [word for word in tokens if word not in stop_words]
# Join the tokens back into a string
 return ' '.join(filtered_tokens)
# Function to find the most similar sentence
def find_most_similar_sentence(input_sentence, file_path):
    # Read the file and preprocess each sentence
 with open(file_path, 'r') as file:
    sentences = file.readlines()
# Preprocess the sentences from the file
 preprocessed_sentences = [preprocess_text(sentence) for sentence in
                          sentences]
# Preprocess the input sentence
 input_sentence_processed = preprocess_text(input_sentence)
# Combine input sentence with sentences from the file for vectorization
 all_sentences = preprocessed_sentences + [input_sentence_processed]
# Initialize the TF-IDF Vectorizer
 vectorizer = TfidfVectorizer()
# Transform the sentences into TF-IDF vectors
 tfidf_matrix = vectorizer.fit_transform(all_sentences)
# Compute cosine similarity between input sentence and all sentences
 cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
# Find the index of the most similar sentence
 most_similar_index = cosine_similarities.argmax()
# Return the most similar sentence
 return sentences[most_similar_index].strip()
# Example usage
input_sentence = "Machine learning is a fascinating field."
file_path = 'sample_text.txt' # Replace with your file path
most_similar_sentence = find_most_similar_sentence(input_sentence,file_path)
print("Most Similar Sentence: Deep learning is a subset of machine learning.")
