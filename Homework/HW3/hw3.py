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
accurs = []
for i in range(1,101):
    model_1=KNeighborsClassifier(n_neighbors=i)
    model_1.fit(x_train,y_train)
    accurs.append(model_1.score(x_test,y_test))
#print(classification_report(y_test, model_1.predict(x_test)))
plt.figure()
plt.plot(list(range(1,101)),accurs)
plt.show()

from sklearn.tree import DecisionTreeClassifier
accurs=[]
for i in range(1,21):
    model_2=DecisionTreeClassifier(max_depth=i,random_state=0)
    model_2.fit(x_train,y_train)
    accurs.append(model_2.score(x_test,y_test))
#print(classification_report(y_test, model_2.predict(x_test)))
plt.figure()
plt.plot(list(range(1,21)),accurs)
plt.show()

from sklearn.ensemble import RandomForestClassifier
accurs=[]
for i in range(1,1000):
    model_3= RandomForestClassifier(n_estimators=i,max_depth=25,random_state=0)
    model_3.fit(x_train,y_train)
    accurs.append(model_3.score(x_test,y_test))
#print(classification_report(y_test, model_3.predict(x_test)))
plt.figure()
plt.plot(list(range(1,1000)),accurs)
plt.show()
