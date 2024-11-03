import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Load data
df = pd.read_csv(r"id3.csv")

# Encode categorical features
enc = LabelEncoder()
df_num_cat = pd.DataFrame()
for col in ["Outlook", "Temperature", "Humidity", "Wind", "PlayTennis"]:
    df_num_cat[col] = enc.fit_transform(df[col])

# Define features and target
x = df_num_cat.drop("PlayTennis", axis=1)
y = df_num_cat["PlayTennis"]

# Train a Decision Tree Classifier
dt_clf = DecisionTreeClassifier(criterion='entropy')
dt_clf.fit(x, y)

# Model predictions and evaluation metrics
y_pred = dt_clf.predict(x)
cf = confusion_matrix(y, y_pred)
acc = accuracy_score(y, y_pred)
pre = precision_score(y, y_pred, average='binary', pos_label=0)
re = recall_score(y, y_pred, average='binary', pos_label=0)

# Predict for a new example
r = dt_clf.predict([[0, 1, 1, 1]])

# Print results
print("Confusion Matrix:\n", cf)
print("Accuracy:", acc)
print("Precision:", pre)
print("Recall:", re)
print("Prediction for [0, 1, 1, 1]:", r)

