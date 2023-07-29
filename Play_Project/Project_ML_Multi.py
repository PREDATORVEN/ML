# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 21:00:58 2023

@author: Yash Sharma
"""
# Python Libraries Used!!
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression 
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import explained_variance_score ,accuracy_score

# DATA PROCESSING & USER_INPUT FUNCTION !!
def data_fetch():
    df=pd.read_csv("Play.csv")
    x=df.iloc[:,1:5].values
    y=df.iloc[:,-1].values
    lab=LabelEncoder()
    for z in range(4):
        x[:,z]=lab.fit_transform(x[:,z])
    y[:,]=lab.fit_transform(y[:,])
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
    
    print('''CHOOSE THE ALGO 
          0.FOR KNN 
          1.FOR LINEAR REGRESSION
          2.FOR LOGISTIC REGRESSION
          ''')
    cho=int(input("Enter your choice:0/1/2 = "))
    if cho==0:
        disp_1(df,x,y,data_arr)
    elif cho==1:
        disp_2(df,x,y,data_arr)
    else:
        disp_3(df,x,y,data_arr)

def disp_1(df,x,y,data_arr):               # FUNC TO CALL KNN ALGO !!
    print("K-NEAREST_NEIGHBOR ALGO")
    algo_1(x, y,data_arr)

def disp_2(df,x,y,data_arr):                # FUNC TO CALL lINEAR_REGRESSION ALGO !!
    print("LINEAR REGRESSION ALGO")
    algo_2(x, y,data_arr)

def disp_3(df,x,y,data_arr):                # FUNC TO CALL LOGISTIC_REGRESSION ALGO !!
    print("LOGISTIC REGRESSION ALGO")
    algo_3(x, y,data_arr)

# KNN ALGO IMPLEMENTATION FUNC !!   
def algo_1(x,y,data_arr):
    y=y.astype('int')
    kn=KNeighborsClassifier()
    kn.fit(x,y)
   
    y2=abs(kn.predict(x))
    y_pred=abs(kn.predict([data_arr]))
    print("-*"*30)
    print("    ")
    print("Prediction -> ",end='')
    if(y_pred.round() ==0):
        print("Can't Play :(")
    else:
        print("Can Play :)")
    
    
    print("Analysis Report!!")
    print("Algo_score:",kn.score(x,y))
    acc=accuracy_score(y, y2)
    print("Accuracy_Score =",acc)
    print("    ")
    print("-*"*30)
    print("Want to Continue ??")
    print('''
          0.To continue
          1.To exit
          ''')
    cot=int(input("Enter your choice.0/1 = "))
    if cot==0:
        main()
    else:
        print("Program Terminated!!")

# LINEAR_REGRESSION IMPLEMENTATION FUNC !!
def algo_2(x,y,data_arr):
    lin=LinearRegression()
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
    var=explained_variance_score(y, y2)
    print("Variance_Score =",var)
    print("    ")
    print("-*"*30)
    print("Want to Continue ??")
    print('''
          0.To continue
          1.To exit
          ''')
    cot=int(input("Enter your choice.0/1 = "))
    if cot==0:
        main()
    else:
        print("Program Terminated!!")
# LOGISTIC_REGRESSION IMPLEMENTATION FUNC !!        
def algo_3(x,y,data_arr):
    y=y.astype('int')
    lr=LogisticRegression()
    lr.fit(x,y)
   
    y2=abs(lr.predict(x))
    y_pred=abs(lr.predict([data_arr]))
    print("-*"*30)
    print("    ")
    print("Prediction -> ",end='')
    if(y_pred.round() ==0):
        print("Can't Play :(")
    else:
        print("Can Play :)")
    
    
    print("Analysis Report!!")
    print("Algo_score:",lr.score(x,y))
    var=explained_variance_score(y, y2)
    print("Variance_Score =",var)
    print("    ")
    print("-*"*30)
    print("Want to Continue ??")
    print('''
          0.To continue
          1.To exit
          ''')
    cot=int(input("Enter your choice.0/1 = "))
    if cot==0:
        main()
    else:
        print("Program Terminated!!") 
# MAIN/DRIVER FUNC!!        
def main():
   data_fetch()
    
main()            