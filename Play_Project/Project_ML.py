# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:55:40 2023

@author: Yash Sharma
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import explained_variance_score,accuracy_score
from sklearn.neighbors import KNeighborsClassifier
def data_fetch(data_arr):
    df=pd.read_csv("Play.csv")
    x=df.iloc[:,1:5].values
    y=df.iloc[:,-1].values
    lab=LabelEncoder()
    for z in range(4):
        x[:,z]=lab.fit_transform(x[:,z])
    y[:,]=lab.fit_transform(y[:,])
    y=y.astype('int')
    display(df,x,y,data_arr)

def display(df,x,y,data_arr):
   algo(x, y,data_arr)

   
    
def algo(x,y,data_arr):
    #lin=LinearRegression()
    lin=KNeighborsClassifier()
    lin.fit(x,y)
   
    y2=abs(lin.predict(x))
    y_pred=abs(lin.predict([data_arr]))
    print("-*"*30)
    print("    ")
    print("Prediction -> ",end='')
    if(y_pred.round() ==0):
        print("Can't Play :(")
    else:
        print("Can Play :)")
    
    
    print("Analysis Report!!")
    print("Algo_score:",lin.score(x,y))
    #var=explained_variance_score(y, y2)
    acc=accuracy_score(y,y2)
#    print("Variance_Score =",var)
    print("Accuracy_score =",acc)    
    print("    ")
    print("-*"*30)
    
    
    
        
    

def main():
    print("PLEASE ENTER THE FOLLOWING DETAILS !!")
    print('''What is the weather?
          0.for Overcast 
          1.for Rainy 
          2.for Sunny ''')
    wea=int(input("Enter your choice:0/1/2 = "))
    print('''What is the temperature?
          0.for Cold
          1.for Hot 
          2.for Mild ''')
  
    temp=int(input("Enter your choice:0/1/2 = "))
    print('''How much humidity?
          0.for High 
          1.for Normal  ''')
    humi=int(input("Enter your choice:0/1 = "))
    print('''What is the wind speed?
          0.for Strong
          1.for Weak ''')
    win=int(input("Enter your choice:0/1 = "))
    
    data_arr=[wea,temp,humi,win]
          
    data_fetch(data_arr)
    
main()    