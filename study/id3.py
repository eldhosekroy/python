import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

df = pd.read_csv(r'data1.csv')
enc = LabelEncoder()

dnc = pd.DataFrame()
dnc['Outlook'] = enc.fit_transform(df['Outlook'])
dnc['Temperature'] = enc.fit_transform(df['Temperature'])
dnc['Humidity'] = enc.fit_transform(df['Humidity'])
dnc['Wind'] = enc.fit_transform(df['Wind'])
dnc['PlayTennis'] = enc.fit_transform(df['PlayTennis'])

x = dnc.drop(['PlayTennis'], axis =1)
y = dnc['PlayTennis']

dt_clf = dtc(criterion='entropy')
dt_clf.fit(x,y)
dt_clf.score(x,y)

y_pred = dt_clf.predict(x)

lbs = [0,1]

acc = accuracy_score(y,y_pred)
cf = confusion_matrix(y,y_pred, labels=lbs)
pre = precision_score(y,y_pred, labels=lbs, pos_label=0)

r = dt_clf.predict([[0,1,1,1]])

print(cf)
print(acc)
print(pre)
print(r)
