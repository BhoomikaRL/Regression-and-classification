import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

possal=pd.read_csv('Position_Salaries.csv')
x=possal.iloc[:,1:2].values
y=possal.iloc[:,2].values

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

linRegressor=LinearRegression()
linRegressor.fit(x,y)

plt.scatter(x,y,color='blue')
plt.plot(x,linRegressor.predict(x),color='red')
plt.show()
list=[]
sc=0
i=1

while(sc<1.0):
    polyFeatures=PolynomialFeatures(degree=i)
    newX=polyFeatures.fit_transform(x)
    linRegressorNew=LinearRegression()
    linRegressorNew.fit(newX,y)
    polyFeatures.fit(newX,y)
    plt.subplot(1,2,2)
    plt.scatter(x,y,color='red')
    plt.plot(x,linRegressorNew.predict(newX),'blue')
    plt.show()
    Score=linRegressorNew.score(newX,y)
    list.append(Score)
    i+=1


    










