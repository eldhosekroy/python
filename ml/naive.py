import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

# Load data
dt = pd.read_csv(r"naive.csv")

# Define features and target
x = dt.iloc[:, :3].values

# Convert target column to categorical if needed
le = LabelEncoder()
y = le.fit_transform(dt.iloc[:, 3].values)

# Split data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Train the Naive Bayes model
model = GaussianNB()
model.fit(x_train, y_train)

# Model predictions
y_pred = model.predict(x_test)

# Input for a new prediction
a = float(input("Sepal length: "))
b = float(input("Sepal width: "))
c = float(input("Petal length: "))
test = model.predict([[a, b, c]])

# Evaluation metrics
print("Prediction for the given input:", le.inverse_transform(test))
print("Accuracy:", model.score(x_test, y_test) * 100)
print("Precision:", precision_score(y_test, y_pred, average='weighted'))
print("Recall:", recall_score(y_test, y_pred, average='weighted'))

