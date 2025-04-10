from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
documents = [
"Data is the new oil in the world of technology.",
"Big data helps in better decision making.",
"The amount of data generated every day is massive."
]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
feature_names = vectorizer.get_feature_names_out()
df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)
print("TF-IDF Matrix:\n")
print(df)
