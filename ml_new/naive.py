import pandas as pd
from sklearn.metrics import precision_score,recall_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

dt=pd.read_csv(r"data.csv")
x=dt.iloc[:,:3].values
y=dt.iloc[:,4].values

x_train,x_test,y_train,y_test=train_test_split(x,y)

model=GaussianNB()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

a=float(input("sepal length:"))
b=float(input("sepal width:"))
c=float(input("petal length:"))

test=model.predict([[a,b,c]])

print(test)
print("Accuracy:",model.score(x,y)*100)
print("precision",precision_score(y_test,y_pred,average=None))
print("Recall",recall_score(y_test,y_pred,average=None))
