# K Nearest Neighbor Libraries 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Decision Tree libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# More Necessary Libraries
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set()

# set up data for Classification of wifi localization in the XY values respectively
wifi_data=pd.read_csv('wifi_localization.txt',sep="\t",names=['S1','S2','S3','S4','S5','S6','S7','Room#'])
X = wifi_data[['S1','S2','S3','S4','S5','S6','S7']].values
Y = wifi_data['Room#'].values

"""
Part I: Self-test for KNN and DT algorithms
"""
knn_self=KNeighborsClassifier(n_neighbors=4)
knn_self.fit(X,Y)
print('KNN Self Test:')
print(classification_report(Y,knn_self.predict(X)))

dtclass_self=DecisionTreeClassifier(max_depth=3, random_state=0)
dtclass_self.fit(X,Y)
print('Decision Tree Self Test:')
print(classification_report(Y,dtclass_self.predict(X)))

"""
Part II: Independent-test for KNN and DT algorithms
"""
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.3,random_state=0)
knn_ind=KNeighborsClassifier(n_neighbors=4)
knn_ind.fit(x_train,y_train)
print('KNN Independent:')
print(classification_report(y_test,knn_ind.predict(x_test)))

dtclass_ind=DecisionTreeClassifier(max_depth=3,random_state=0)
dtclass_ind.fit(x_train,y_train)
print('Decision Tree Independent:')
print(classification_report(y_test,dtclass_ind.predict(x_test)))

"""
Part III: Classification Model Finalization

# constructing a final model based on the analysis above
final_model=''

# illustrating a confusion matrix of the final model
 
# Graphing Results of the Independent Tests from 10-50% of the data utilized
model_scores=[]
percentages=[0.1,0.2,0.3,0.4,0.5]
for i in percentages:
    x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=i,random_state=0)
    final_model.fit(x_train,y_train)
    model_scores.append(final_model.score(x_test,y_test))

plt.plot(percentage,knn_scores,label='Model Performance',color='red')
plt.xlabel('Percentage of Data Used')
plt.ylabel('Model Performance Score')
plt.title('Model Perfomance: Percentage of Data Used')
plt.legend()
plt.show()
plt.savefig('scores_independent.png')
"""