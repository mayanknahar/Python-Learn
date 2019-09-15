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
imputer=Imputer(missing_values=np.nan, strategy="mean", axis=0)   # imputer transformer for completing missing values
imputer=imputer.fit(x[:,1:3])
x[:, 1:3]=imputer.transform(x[:, 1:3])

#encoding categorial data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_x=LabelEncoder()   #numeric transform of data for analysis purpose
x[:,0]=labelEncoder_x.fit_transform(x[:,0])
onehotencoder=OneHotEncoder(categorical_features=[0]) #divides individual columns of each categorial data
x=onehotencoder.fit_transform(x).toarray()
labelEncoder_y=LabelEncoder()
y=labelEncoder_y.fit_transform(y)

#splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
#20% is used for testing phase and rest for training phase
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

#Feature Scaling which will help in machine learning model (Eucledian Distance)
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)    #scaling done is fitted in the training set
x_test=sc_x.transform(x_test)          #so fiting in test case is not necessary
