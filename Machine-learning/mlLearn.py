# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:01:20 2019

@author: Marcos
"""
#Data Preprocessing

#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing Dataset
dataset=pd.read_csv('Data1.csv')  #this loads the dataset
x=dataset.iloc[:,:-1].values     #this is the extraction of data 
y=dataset.iloc[:,3].values

#Find the missing values by finding the mean 
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values=np.nan, strategy="mean", axis=0)
imputer=imputer.fit(x[:,1:3])
x[:, 1:3]=imputer.transform(x[:, 1:3])

#encoding categorial data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_x=LabelEncoder()
x[:,0]=labelEncoder_x.fit_transform(x[:,0])
onehotencoder=OneHotEncoder(categorical_features=[0])
x=onehotencoder.fit_transform(x).toarray()
labelEncoder_y=LabelEncoder()
y=labelEncoder_y.fit_transform(y)


