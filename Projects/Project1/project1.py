# K Nearest Neighbor Libraries 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Decision Tree libraries
from sklearn.tree import DecisionTreeClassifier

# More Necessary Libraries
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set()

# set up data for Classification of wifi localization in the XY values respectively
wifi_data=pd.read_csv('wifi_localization.txt',sep="\t",names=['S1','S2','S3','S4','S5','S6','S7','Room#'])
X = wifi_data[['S1','S2','S3','S4','S5','S6','S7']].values
Y = wifi_data['Room#'].values
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.3,random_state=0)
knn_model=KNeighborsClassifier(n_neighbors=39)
dt_model=DecisionTreeClassifier(max_depth=3, random_state=0)

"""
Part I: Self-test for KNN and DT algorithms
"""

# Here for the self test the training data is the test data
knn_model.fit(x_train,y_train) # training the model
print('KNN Self Test:')
y_predict=knn_model.predict(x_train)
print(classification_report(y_train,y_predict))

dt_model.fit(x_train,y_train)
y_predict=dt_model.predict(x_train)
print('Decision Tree Self Test:')
print(classification_report(y_train,y_predict))

"""
Part II: Independent-test for KNN and DT algorithms
"""

# independent test a certain percentage of data set is used as the testing data
# while the remaining percentage is used as the training data. (30/70 split used here)
knn_model.fit(x_train,y_train)
y_predict=knn_model.predict(x_test)
print('KNN Independent:')
print(classification_report(y_test,y_predict))

dt_model.fit(x_train,y_train)
y_predict=dt_model.predict(x_test)
print('Decision Tree Independent:')
print(classification_report(y_test,y_predict))

"""
Part III: Classification Model Finalization
"""
# constructing a final model based on the analysis above and different approaches and experiments
final_model=knn_model
final_model.fit(x_train,y_train)
y_predict=final_model.predict(x_test)
print('Final Model Report:')
print(classification_report(y_test, y_predict))

# illustrating a confusion matrix of the final model
cmatrix=confusion_matrix(y_test, y_predict)

# Note: Inspiration for illutrating confusion matrix came from Module 5.1: KNN Neighbors & ML
fig, ax = plt.subplots(figsize=(2, 2))
ax.matshow(cmatrix, cmap=plt.cm.Blues, alpha=0.3)
for i in range(cmatrix.shape[0]):
    for j in range(cmatrix.shape[1]):
        ax.text(x=j, y=i,s=cmatrix[i, j], va='center', ha='center', size='large')
plt.xlabel('Predictions', fontsize=10)
plt.ylabel('Actuals', fontsize=10)
plt.title('Confusion Matrix', fontsize=10)
plt.show()

# Line Graph: Results of the Independent Tests from 10-50% of the data utilized
# for testing purposes and rest for training the finalized model
model_scores=[]
percentages=[i/10 for i in range(1,6)]
for i in percentages:
    x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=i,random_state=0)
    final_model.fit(x_train,y_train)
    model_scores.append(final_model.score(x_test,y_test))

plt.plot(percentages,model_scores,label='Model Performance',color='red')
plt.scatter(percentages,model_scores,color='red')
plt.xlabel('Percentage of Data Used')
plt.ylabel('Model Performance Score')
plt.title('Model Perfomance: Percentage of Data Used')
plt.legend()
plt.show()
