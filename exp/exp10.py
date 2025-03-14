from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score

# Expanded Dataset

texts = [

 "I love sunny days", "Rainy weather is the worst", "I enjoy going to thebeach",
 "The movie was fantastic", "I hated the film", "What an amazing experience",
 "It's too cold outside", "Warm weather makes me happy", "That book was boring",
 "The concert was incredible", "Terrible acting in that movie", "Best food I've ever had",
 "The service was awful", "Beautiful scenery", "I dislike bad movies",
 "Horrible customer service", "Absolutely loved it", "The place was dirty",
 "The staff was friendly", "Not worth the money"]

labels = ['positive', 'negative', 'positive', 'positive', 'negative','positive', 'negative', 'positive', 'negative', 'positive',

 'negative', 'positive', 'negative', 'positive', 'negative',

 'negative', 'positive', 'negative', 'positive', 'negative']
vectorizer = TfidfVectorizer(ngram_range=(1, 3), max_features=500, 
stop_words='english')
X = vectorizer.fit_transform(texts)
# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
 X, labels, test_size=0.2, random_state=42, stratify=labels
)
# Naïve Bayes Model (better for small datasets)
model = MultinomialNB()
model.fit(X_train, y_train)
# Evaluate Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", round(accuracy * 100, 2), "%")
# Test New Samples
new_text = ["The weather is beautiful", "I dislike bad movies"]
new_X = vectorizer.transform(new_text)
predictions = model.predict(new_X)
for text, label in zip(new_text, predictions):
 print(f"Text: '{text}' → Predicted Sentiment: {label}")
