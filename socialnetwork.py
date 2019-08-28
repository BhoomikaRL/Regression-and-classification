
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

social=pd.read_csv('Social_Network_Ads.csv')
x=social.iloc[:,2:4].values
y=social.iloc[:,4].values

from sklearn.preprocessing import StandardScaler

sScaler=StandardScaler()

x=sScaler.fit_transform(x)

#split the data

from sklearn.linear_model import LogisticRegression

lClassifier=LogisticRegression()
lClassifier.fit(x,y)

y_pred=lClassifier.predict(x)

j=0
count=0
for i in y:
    if i==y_pred[j]:
        count+=1
    j+=1
print("number of matches are ={0}".format(count))
print("number of mis matches are={0}".format(j-count))

a=int(input("enter the age"))
b=int(input("enter the salary"))
list=[]
list.append(a)
list.append(b)
p=np.array(list)
p=p.reshape(1,-1)
p1=sScaler.transform(p)
y_prediction=lClassifier.predict(p1)


    


