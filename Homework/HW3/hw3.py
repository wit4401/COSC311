import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from seaborn import set, heatmap
set()

col_label=[str(i) for i in range(1,66)]+['Class']
food_data = pd.read_csv('FoodTypeDataset.csv',names=col_label)
X=food_data[col_label[:65]].values
Y=food_data['Class'].values
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

# checking out KNearestNeighbors classificaiton model
knn = KNeighborsClassifier(n_neighbors=16)
knn.fit(x_train,y_train)
print('KNN Score:',knn.score(x_test,y_test))
accurs = []
for i in range(1,101):
    model_1=KNeighborsClassifier(n_neighbors=i)
    model_1.fit(x_train,y_train)
    accurs.append(model_1.score(x_test,y_test))
plt.figure()
plt.plot(list(range(1,101)),accurs)
plt.xlabel('k')
plt.ylabel('avg accuracy')
plt.title('KNN Accuracy based off k value')
plt.show()

# checking out Decision Tree classification model
dt = DecisionTreeClassifier(max_depth=17,random_state=0)
dt.fit(x_train,y_train)
print('Decision Tree Score:',dt.score(x_test,y_test))
accurs=[]
for i in range(1,101):
    model_2=DecisionTreeClassifier(max_depth=i,random_state=0)
    model_2.fit(x_train,y_train)
    accurs.append(model_2.score(x_test,y_test))
plt.figure()
plt.plot(list(range(1,101)),accurs)
plt.xlabel('max_depth')
plt.ylabel('avg accuracy')
plt.title('Decision Tree Accuracy based off max_depth')
plt.show()

# checking Random Forest Classification Model
rand_forest = RandomForestClassifier(n_estimators=750,max_depth=10,random_state=0)
rand_forest.fit(x_train,y_train)
print('Random Forest Score:',rand_forest.score(x_test,y_test))

# checking Support Vector Machine classification model
svm = SVC(kernel='linear',decision_function_shape='ovo',random_state=0)
svm.fit(x_train,y_train)
print('Support Vector Machine Score:',svm.score(x_test,y_test))

print('\nBest accuracy: Support Machine Vector model')
print(classification_report(y_test,svm.predict(x_test)))

conf_matrix = confusion_matrix(y_test,svm.predict(x_test))
heatmap(conf_matrix,annot=True)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()
