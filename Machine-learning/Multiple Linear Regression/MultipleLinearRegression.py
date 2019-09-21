# Multiple Regression

#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing Dataset
dataset=pd.read_csv('50_Startups.csv')  #this loads the dataset
x=dataset.iloc[:,:-1].values     #this is the extraction of data 
y=dataset.iloc[:,4].values

#Encoding categorial data
#encoding of Independent Variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_x=LabelEncoder()   #numeric transform of data for analysis purpose
x[:,3]=labelEncoder_x.fit_transform(x[:,3])
onehotencoder=OneHotEncoder(categorical_features=[3]) #divides individual columns of each categorial data
x=onehotencoder.fit_transform(x).toarray()

#Avoiding the Dummy Variable Trap i.e. removing one column of dummy variable
x=x[:,1:]


#Splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
#20% is used for testing phase and rest for training phase
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

'''#Feature Scaling which will help in machine learning model (Eucledian Distance)
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)    #scaling done is fitted in the training set
x_test=sc_x.transform(x_test)          #so fiting in test case is not necessary'''

#Fitting Multiple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

#Predicting the Test set results
y_pred=regressor.predict(x_test)
