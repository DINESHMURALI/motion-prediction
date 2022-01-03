# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 15:38:17 2022

@author: Admin
"""
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

data = pd.read_csv('data.csv')

Tilt_left = data[data['Position']=='Tilt left'].head(1233).copy()
Resting = data[data['Position']=='Resting'].head(1233).copy()
Tilt_Right = data[data['Position']=='Tilt Right'].copy()

balanced_data = pd.DataFrame()
balanced_data = balanced_data.append([Tilt_left, Resting, Tilt_Right])


x_data = balanced_data.drop(['Position'],axis=1)
y_data = balanced_data['Position']
MinMaxScaler = preprocessing.MinMaxScaler()
X_data_minmax = MinMaxScaler.fit_transform(x_data)
data = pd.DataFrame(X_data_minmax,columns=['X', 'Y', 'Z'])

X_train, X_test, y_train, y_test = train_test_split(data, y_data,test_size=0.2, random_state = 1, stratify = y_data)
knn=KNeighborsClassifier()
knn.fit(X_train,y_train)
ypred=knn.predict(X_test)

pickle.dump(knn, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1.44, 9.56, 1.53]]))



