import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

profit=pd.read_csv('50_Startups.csv')
x=profit.iloc[:,:4].values
y=profit.iloc[:,4].values

from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import OneHotEncoder

lEncoder=LabelEncoder()
x[:,3]=lEncoder.fit_transform(x[:,3])

ohEncoder=OneHotEncoder(categorical_features=[3])
x= ohEncoder.fit_transform(x).toarray()
x=x[:,1:]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,test_size=0.2)

from sklearn.linear_model import LinearRegression
mRegressor=LinearRegression()

mRegressor.fit(x_train,y_train)
y_pred=mRegressor.predict(x_test)

import statsmodels.formula.api as sm 

a=np.ones((50,1))
x=np.append(a,x,axis=1)

xopt=x[:,[0,3]]

sm.OLS(endog=y, exog=xopt).fit().summary()

newMRegressor=LinearRegression()
xoptTrain,xoptTest,yoptTrain,yoptTest=train_test_split(xopt,y,random_state=0,test_size=0.2)

newMRegressor.fit(xoptTrain,yoptTrain)
ypredOPT=newMRegressor.predict(xoptTest)




