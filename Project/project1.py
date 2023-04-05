# K Nearest Neighbor Libraries 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# Decision Tree libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# More Necessary Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set()

# set up data for Classification of wifi localization
wifi_data=pd.read_csv('wifi_localization.txt',sep="\t",names=['S1','S2','S3','S4','S5','S6','S7','Room#'])
print(wifi_data.info())

"""
Part I: Self-test for KNN and DT algorithms
"""
room1=wifi_data[wifi_data['Room#']==1]
room2=wifi_data[wifi_data['Room#']==2]
room3=wifi_data[wifi_data['Room#']==3]
room4=wifi_data[wifi_data['Room#']==4]

"""
Part II: Independent-test for KNN and DT algorithms
"""

"""
Part III: Classification Model Finalization
"""
