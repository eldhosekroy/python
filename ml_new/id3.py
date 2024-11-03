import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
df = pd.read_csv(r"data1.csv")
enc = LabelEncoder()

dnc = pd.DataFrame()
dnc["Outlook"] = enc.fit_transform(df["Outlook"])
dnc["Temperature"] = enc.fit_transform(df["Temperature"])
dnc["Humidity"] = enc.fit_transform(df["Humidity"])
dnc["Wind"] = enc.fit_transform(df["Wind"])
dnc["PlayTennis"] = enc.fit_transform(df["PlayTennis"])

x = dnc.drop(["PlayTennis"])
y = dnc["PlayTennis"]
dt_clf = dtc(criterion='entropy')
dt_clf.fit(x,y)
dt_clf.score(x,y)

y_pred=dt_clf.predict(x)

lbs = [0,1]

cf = confusion_matrix(y,y_pred,labels=lbs)
acc = accuracy_score(y,y_pred)
pre = precision_score(y,y_pred,labels=lbs,pos_label=0)
re = recall_score(y,y_pred,labels=lbs,pos_label=0)

r = dt_clf.predict([[0,1,1,1]])

print("confusion_matrix:\n",cf)
print("accuracy",acc)
print("precision",pre)
print("recall",re)
print("class",r)
