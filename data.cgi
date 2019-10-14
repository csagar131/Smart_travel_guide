#!/usr/bin/python3

import cgi, cgitb


import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# Create instance of FieldStorage
form = cgi.FieldStorage()

# getting form value
gender = form.getvalue('gender')
age = form.getvalue('age')
cp = form.getvalue('cp')
trestbps = form.getvalue('trestbps')
chol = form.getvalue('chol')
fbs = form.getvalue('fbs')
restecg = form.getvalue('restecg')
thalach = form.getvalue('thalach')
exang = form.getvalue('exang')
oldpeak = form.getvalue('oldpeak')
slope = form.getvalue('slope')
ca = form.getvalue('ca')
thal = form.getvalue('thal')


# machine learning code

df = pd.read_csv('http://13.233.94.154/heart.csv')


features = df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']]
features = features.fillna(features.mean())
features = features.values
label = df[['target']].values

x_train,x_test,y_train,y_test = train_test_split(features,label,test_size=0.01,random_state=4)
clf = RandomForestClassifier(criterion='entropy',n_estimators=7)


trained = clf.fit(x_train,y_train)
predicted = trained.predict(x_test)

from numpy import array
a = array( [age,gender,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal] )


a.reshape(-1,1)
result = list(trained.predict([a]))[0]

#---------------------------------------------------------------------------------------------------------------------------
# html printing part

print("Content-type:text/html\r\n\r\n")

a ='''
<div align="center">
<h2> Ohh! You may have heart disease. </h2>
<p>
<img src='http://13.233.94.154/positive.jpg'/>
</p>

<style>
.button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 5px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}



</style>


<form action = '/cgi-bin/maps.cgi' method = "GET" >
<input class='box' type='text' placeholder='  Enter city' name='city' width='48' height='48'  required /></br>
<input type='submit'  class='button'"    value='Find Doctors' /></br>
</form>
</div>
'''

show0 = '''
<html>
<head>
<title>Heart Disease Predictor</title>
</head>
<body>
<h1>Heart disease predictor is here where are you??\n\n</h1>
'''

show1 = '''
<div align='center'>
<h2> You dont have heart disease. </h2>
<p>
<img src='http://13.233.94.154/negative.jpg'/>
</p>
</div>
'''

print(show0)

if result == 0:
	print(show1)
else:
	print(a)


