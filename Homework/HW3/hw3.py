import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

col_label=[str(i) for i in range(1,66)]+['Class']
food_data = pd.read_csv('FoodTypeDataset.csv',names=col_label)
X=food_data[col_label[:65]].values
Y=food_data['Class'].values
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

from sklearn.neighbors import KNeighborsClassifier

model_1=KNeighborsClassifier(n_neighbors=2)
model_1.fit(x_train,y_train)
print(classification_report(y_test, model_1.predict(x_test)))

from sklearn.tree import DecisionTreeClassifier

model_2=DecisionTreeClassifier(random_state=0)
model_2.fit(x_train,y_train)
print(classification_report(y_test, model_2.predict(x_test)))

from sklearn.ensemble import RandomForestClassifier

model_3= RandomForestClassifier(n_estimators=750,max_depth=25,random_state=0)
model_3.fit(x_train,y_train)
print(classification_report(y_test, model_3.predict(x_test)))
