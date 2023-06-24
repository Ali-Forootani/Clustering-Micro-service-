
import json
import math
import time
import pandas as pd
import os
import sklearn
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
from sklearn.neural_network import MLPRegressor
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import KMeans
import nltk
import networkx as nx
from sklearn.cluster import Birch
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import OPTICS
import kmeans1d
from pandas import read_excel
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pickle
from time import sleep
from json import loads
from time import sleep
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pickle





class time_computation_function:
    def __init__(self,x,schedul,s_t):
        self.x=x #x is pick_up time or delivery time
        self.schedul=schedul
        self.s_t=s_t
    

    @staticmethod
    def CheckLeap(Year):  
        # Checking if the given year is leap year  
        if((Year % 400 == 0) or (Year % 100 != 0) and  (Year % 4 == 0)):   
            #print("Given Year is a leap Year")
            leap_year="true"
            # Else it is not a leap year  
        else:  
            #print ("Given Year is not a leap Year")  
            leap_year="false"
        return leap_year



    def universal_time_mapping(self):
        y=np.zeros((self.s_t,1))
        j=0

        if self.schedul[0] == "Yearly":
            for i in self.x:

                leap_year=self.CheckLeap(i.year)

                #print(leap_year)

                if i.month==4 or i.month==5 or i.month==9 or i.month==11:
                    y[j,0]=int(i.year)*365*24*60+int(i.month)*30*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
                elif i.month==2 and leap_year=="false":
                    y[j,0]=int(i.year)*365*24*60+int(i.month)*28*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
                elif i.month==2 and leap_year=="true":
                    y[j,0]=int(i.year)*365*24*60+int(i.month)*29*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
                else:
                    y[j,0]=int(i.year)*365*24*60+int(i.month)*31*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
                j=j+1
        if self.schedul[0] == "Monthly":

            #print("I am here")

            for i in self.x:

                leap_year=self.CheckLeap(i.year)

                #print(leap_year)

                if i.month==4 or i.month==5 or i.month==9 or i.month==11:
                    y[j,0]=int(i.month)*30*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
                elif i.month==2 and leap_year=="false":
                    y[j,0]=int(i.month)*28*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
                elif i.month==2 and leap_year=="true":
                    y[j,0]=int(i.month)*29*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
                else:
                    y[j,0]=int(i.month)*31*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
                j=j+1

        
        if self.schedul[0] == "Weekly":
            for i in self.x:
                y[j,0]=int(i.day)*24*60+int(i.hour)*60+int(i.minute)            
                j=j+1
        if self.schedul[0]=="Daily":
            for i in self.x:
                y[j,0]=int(i.hour)*60+int(i.minute)
                j=j+1
        y=np.reshape(y,(self.s_t,1))

        return y


    def run(self):

        y=self.universal_time_mapping()

        return y
        




###############
###############
###############
###############


#def time_computation_function(x,schedul,s_t):
    
    # Later on we should select ``daily''-``weekly''-``montly''-``yearly'' switch-case conditional statement
#    y=np.zeros((s_t,1))
#    j=0
    
    #print(schedul[0])

#    if schedul[0]=="Yearly":
#        for i in x:

            #Leap year checking
#            def CheckLeap(Year):  
                # Checking if the given year is leap year  
#                if((Year % 400 == 0) or (Year % 100 != 0) and  (Year % 4 == 0)):   
                    #print("Given Year is a leap Year")
#                    leap_year="true"
                # Else it is not a leap year  
#                else:  
                    #print ("Given Year is not a leap Year")  
#                    leap_year="false"
#                return leap_year

#            leap_year=CheckLeap(i.year)

            #print(leap_year)

#            if i.month==4 or i.month==5 or i.month==9 or i.month==11:
#                y[j,0]=int(i.year)*365*24*60+int(i.month)*30*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
#            elif i.month==2 and leap_year=="false":
#                y[j,0]=int(i.year)*365*24*60+int(i.month)*28*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
#            elif i.month==2 and leap_year=="true":
#                y[j,0]=int(i.year)*365*24*60+int(i.month)*29*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
#            else:
#                y[j,0]=int(i.year)*365*24*60+int(i.month)*28*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
#            j=j+1
#    if schedul[0]== "Monthly":

        #print("I am here")

#        for i in x:

            #Leap year checking
#            def CheckLeap(Year):  
                # Checking if the given year is leap year  
#                if((Year % 400 == 0) or (Year % 100 != 0) and  (Year % 4 == 0)):   
                    #print("Given Year is a leap Year")
#                    leap_year="true"
                # Else it is not a leap year  
#                else:  
                    #print ("Given Year is not a leap Year")  
#                    leap_year="false"
#                return leap_year

#            leap_year=CheckLeap(i.year)

            #print(leap_year)


#            if i.month==4 or i.month==5 or i.month==9 or i.month==11:
#                y[j,0]=int(i.month)*30*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
#            elif i.month==2 and leap_year=="false":
#                y[j,0]=int(i.month)*28*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
#            elif i.month==2 and leap_year=="true":
#                y[j,0]=int(i.month)*29*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
#            else:
#                y[j,0]=int(i.month)*28*24*60+int(i.day)*24*60+int(i.hour)*60+int(i.minute)
#            j=j+1
#    if schedul[0]=="Weekly":
#        for i in x:
#            y[j,0]=int(i.day)*24*60+int(i.hour)*60+int(i.minute)            
#            j=j+1
#    if schedul[0]=="Daily":
#        for i in x:
#            y[j,0]=int(i.hour)*60+int(i.minute)
#            j=j+1
#    y=np.reshape(y,(s_t,1))

#    return y
