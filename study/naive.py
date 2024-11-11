import pandas as pd
from sklearn.metrics import precision_score, recall_score
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

dt = pd.read_csv(r'data.csv')
x = dt.iloc[:, :3].values
y = dt.iloc[:, 4].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

model = GaussianNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

a = float(input("Petal length: "))
b = float(input("Petal width: "))
c = float(input("Sepal length: "))

test_prediction = model.predict([[a, b, c]])
print("Prediction:", test_prediction)

print("Test Accuracy:", model.score(x_test, y_test) * 100)
print("Precision:", precision_score(y_test, y_pred, average=None, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, average=None, zero_division=0))
