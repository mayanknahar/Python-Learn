#Simple Linear Regression

#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing Dataset
dataset=pd.read_csv('Salary_Data.csv')  #this loads the dataset
x=dataset.iloc[:,:-1].values     #this is the extraction of data excluding last column
y=dataset.iloc[:,1].values

#splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)

#Feature Scaling which will help in machine learning model (e.g Eucledian Distance)
"""from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)    #scaling done is fitted in the training set
x_test=sc_x.transform(x_test)          #so fiting in test case is not necessary"""

#Fitting Simple Linear Regression into the training set
from sklearn.linear_model import LinearRegression
#Here machine is the Linear Regresson which is trained on our dataset
regressor=LinearRegression()      #Object of the linearregression class is generated
regressor.fit(x_train,y_train)   #fits the linear regression model with the training set