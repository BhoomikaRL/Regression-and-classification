from flask import Flask,render_template,request
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io
import base64

salary=pd.read_csv('Salary_Data.csv')
x=salary.iloc[:,0:1].values
y=salary.iloc[:,1].values
plt.scatter(x,y,color='red')

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,test_size=1/3)

from sklearn.linear_model import LinearRegression
sRegressor=LinearRegression()
app=Flask(__name__,static_folder='public')


@app.route('/')
def index():
    sRegressor.fit(x_train,y_train)
    y_pred=sRegressor.predict(x_test)
    plt.subplot(1,2,1)
    plt.scatter(x_train,y_train,color='blue')
    plt.plot(x_train,sRegressor.predict(x_train),'r')
    plt.subplot(1,2,2)
    plt.scatter(x_test,y_test,color='blue')
    plt.plot(x_test,sRegressor.predict(x_test),'r')
    img=io.BytesIO()
    plt.savefig(img,format='png')
    graphUrl=(img.getvalue())
    return render_template('index.html',graphInfo=graphUrl)
    



if __name__=='__main__':
    app.run(debug=True)
    

