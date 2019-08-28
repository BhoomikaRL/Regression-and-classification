from sklearn.datasets import  load_iris
iris=load_iris()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x=iris.data[:,:4]
y=iris.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,test_size=0.2)

from sklearn.linear_model import LinearRegression
mRegressor=LinearRegression()

mRegressor.fit(x_train,y_train)
y_pred=mRegressor.predict(x_test)

import statsmodels.formula.api as sm 

a=np.ones((150,1))
x=np.append(a,x,axis=1)

xopt=x[:,[1,3,4]]

sm.OLS(endog=y, exog=xopt).fit().summary()

newMRegressor=LinearRegression()
xoptTrain,xoptTest,yoptTrain,yoptTest=train_test_split(xopt,y,random_state=0,test_size=0.2)

newMRegressor.fit(xoptTrain,yoptTrain)
ypredOPT=newMRegressor.predict(xoptTest)

