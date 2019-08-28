import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

possal=pd.read_csv('Position_Salaries.csv')
x=possal.iloc[:,1:2].values
y=possal.iloc[:,2].values

#plt.scatter(x,y,color='red')
#plt.plot(x,y,color='blue')

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

linRegressor=LinearRegression()
linRegressor.fit(x,y)

plt.scatter(x,y,color='blue')
plt.plot(x,linRegressor.predict(x),color='red')
plt.show()

#for polynomial regression
polyFeatures=PolynomialFeatures(degree=6)

newX=polyFeatures.fit_transform(x)

linRegressorNew=LinearRegression()
linRegressorNew.fit(newX,y)

polyFeatures.fit(newX,y)

plt.scatter(x,y,color='red')
plt.plot(x,linRegressorNew.predict(newX),'blue')

y_pred=linRegressorNew.predict(newX)

#to predict the value for 3.5 level
#method1
z=[3.5]
z=np.array(z).reshape(1,-1)
newZ=polyFeatures.fit_transform(z)
y_pred_new=linRegressorNew.predict(newZ)

#method2
linRegressorNew.predict(polyFeatures.fit_transform([[3.5]]))







