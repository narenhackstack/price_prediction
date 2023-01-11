# -*- coding: utf-8 -*-
"""multilocation-ds2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nTFcmX88ebqTSHO_kVnX5VT9ig1PHoSM

# To find the price of the house when the location and area in sqft is given.
"""

import pandas as pd

df=pd.read_csv('/content/multilocation - Sheet1.csv')
df

"""#One Hot Encoding technique 
Since we are having more than 1 location data we cannot directly train it! So we need to convert the cities/area into a numerical value. But we cannot assign like City1 - 1, City2 - 2 like categorizing. Because ML will understand that as direct value and not as a category! So we are going to use a technique called as One Hot Encoding!

One Hot Encoding ( OHE ) technique will create a dummy values for the respective columns and row values.

For example: For area column in this data set we are going to use OHE and create the following thing


"""

#create a variable to store a dummy valeues
dummies=pd.get_dummies(df.area)
dummies

mergeddf=pd.concat([df,dummies],axis='columns')
mergeddf

mergeddf

#dimensionality reduction
finaldf=mergeddf.drop(['area','Saibaba Colony'],axis=1)
finaldf

X=finaldf.drop('price',axis=1)

len(X.columns)

y=finaldf.price

"""#Building the Machine Learning model """

from sklearn import linear_model

reg=linear_model.LinearRegression()

reg.fit(X,y)

reg.predict([[2000,0,1,0,0]])

reg.predict([[2000,0,0,0,1]])

reg.predict([[2000,0,0,0,0]])

"""#Creating predictive System"""

import numpy as np

def predictprice(location,sqft):
    # we have to write the logic so that will get like below format
    #reg.predict([[2000,0,0,0,0]])
    
    #need to create a numpy array with 0, for X length x=[0,0,0,0,0]
    #x[0]=sqft --> x=[sqft,0,0,0,0]
    #we have to find out the index of that particular location in the X value iin the variable locindex
    #locindex=3
    #x[3]=1 x=[sqft,0,0,1,0]
    #step1: #need to create a numpy array with 0, for X length x=[0,0,0,0,0]
    x=np.zeros(len(X.columns)) 
    #step2:#x[0]=sqft --> x=[sqft,0,0,0,0]
    x[0]=sqft
    #step 3:    #we have to find out the index of that particular location in the X value iin the variable locindex
    locindex=np.where(X.columns==location)[0][0]
    #step 4: allocate value 1 in the found index
    if locindex>=0:
        x[locindex]=1 #--> x=[sqft,0,0,1,0]
    return reg.predict([x])[0]

np.where(X.columns=='R.S.Puram')[0][0]

location=input("Enter the location")
sqft=int(input("Enter the sqft"))
predictedprice=predictprice(location,sqft)
print(predictedprice)

locindex=np.where(X.columns==location)[0][0]

"""#Downloading the Model"""

import pickle
with open('Multilocationmodelds2','wb')as f:
  pickle.dump(reg,f)

"""#Downloading the columns"""

import json

columns={
    'Data_columns':[col.lower()for col in X.columns]
}
with open('columns.json','w')as f:
  f.write(json.dumps(columns))
