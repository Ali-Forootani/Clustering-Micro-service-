


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


class time_scheduling_function:
    def __init__(self,Pic_Year,Pic_Month,Pic_Day,Pic_Hour,Del_Year,Del_Month,Del_Day,Del_Hour):
        self.Pic_Year=Pic_Year
        self.Pic_Month=Pic_Month
        self.Pic_Day=Pic_Day
        self.Pic_Hour=Pic_Hour
        self.Del_Year=Del_Year
        self.Del_Month=Del_Month
        self.Del_Day=Del_Day
        self.Del_Hour=Del_Hour

    # Raising some exceptions if the input data was not in a list format

    def not_list_test_functions(self):

        if not isinstance(self.Pic_Year, list):
            raise Exception("Pickup time Year is a list, please make sure we have a list")
        if not isinstance(self.Pic_Month, list):
            raise Exception("Pickup time Month is a list, please make sure we have a list")
        if not isinstance(self.Pic_Day, list):
            raise Exception("Pickup time Day is a list, please make sure we have a list")
        if not isinstance(self.Pic_Hour, list):
            raise Exception("Pickup time Hour is a list, please make sure we have a list")
        if not isinstance(self.Del_Year, list):
            raise Exception("Delivery time Year is a list, please make sure we have a list")
        if not isinstance(self.Del_Month, list):
            raise Exception("Delivery time Month is a list, please make sure we have a list")
        if not isinstance(self.Del_Day, list):
            raise Exception("Delivery time Day is a list, please make sure we have a list")
        if not isinstance(self.Del_Hour, list):
            raise Exception("Delivery time Hour is a list, please make sure we have a list")

    # Raising some exceptions if the input data has negative element for year, month, day or hour

    def negative_element_in_lists(self):
        if any(x<0 for x in self.Pic_Year):
             raise Exception("Pickup time Year has a negative member, please make sure Year is a positive quantity")
        if any(x<0 for x in self.Pic_Month):
             raise Exception("Pickup time Month has a negative member, please make sure Month is a positive quantity")
        if any(x<0 for x in self.Pic_Day):
             raise Exception("Pickup time Day has a negative member, please make sure Day is a positive quantity")
        if any(x<0 for x in self.Pic_Hour):
             raise Exception("Pickup time Hour has a negative member, please make sure Day is a positive quantity")
        if any(x<0 for x in self.Del_Year):
             raise Exception("Delivery time Year has a negative member, please make sure Year is a positive quantity")
        if any(x<0 for x in self.Del_Month):
             raise Exception("Delivery time Month has a negative member, please make sure Month is a positive quantity")
        if any(x<0 for x in self.Del_Day):
             raise Exception("Delivery time Day has a negative member, please make sure Day is a positive quantity")
        if any(x<0 for x in self.Del_Hour):
             raise Exception("Delivery time Hour has a negative member, please make sure Day is a positive quantity")

    def max_min_determination(self):
        min_Pic_Year=min(self.Pic_Year)
        max_Pic_Year=max(self.Pic_Year)
        max_Pic_Month=max(self.Pic_Month)
        min_Pic_Month=min(self.Pic_Month)
        max_Pic_Day=max(self.Pic_Day)
        min_Pic_Day=min(self.Pic_Day)
        max_Pic_Hour=max(self.Pic_Hour)
        min_Pic_Hour=min(self.Pic_Hour)

        min_Del_Year=min(self.Del_Year)
        max_Del_Year=max(self.Del_Year)
        max_Del_Month=max(self.Del_Month)
        min_Del_Month=min(self.Del_Month)
        max_Del_Day=max(self.Del_Day)
        min_Del_Day=min(self.Del_Day)
        max_Del_Hour=max(self.Del_Hour)
        min_Del_Hour=min(self.Del_Hour)

        if int(min_Pic_Year) > int(max_Del_Year):
            raise Exception("The global max delivery time has to be greater than global min")

        return min_Pic_Year,max_Pic_Year,max_Pic_Month,min_Pic_Month,max_Pic_Day,min_Pic_Day\
                ,max_Pic_Hour,min_Pic_Hour,min_Del_Year,max_Del_Year,max_Del_Month,min_Del_Month\
                ,max_Del_Day,min_Del_Day


    def shceduling_computation(self,min_Pic_Year,max_Pic_Year,max_Pic_Month,min_Pic_Month,max_Pic_Day,min_Pic_Day\
                ,max_Pic_Hour,min_Pic_Hour,min_Del_Year,max_Del_Year,max_Del_Month,min_Del_Month\
                ,max_Del_Day,min_Del_Day):
        schedule=[]
        if int(max_Del_Year) - int(min_Pic_Year) > 0:
            schedule.append("Yearly")
        elif int(max_Del_Month) - int(min_Pic_Month) > 0 and int(max_Del_Year) == int(min_Pic_Year):
            schedule.append("Monthly")
        
        elif int(max_Del_Day) - int(min_Pic_Day) > 0 and int(max_Del_Month) == int(min_Pic_Month) and int(max_Del_Year) == int(min_Pic_Year):
            schedule.append("Weekly")
        
        elif int(max_Del_Day) == int(min_Pic_Day) and int(max_Del_Month) == int(min_Pic_Month) and int(max_Del_Year) == int(min_Pic_Year):
            schedule.append("Daily")

        return schedule

    def run(self):
        self.not_list_test_functions()


        min_Pic_Year,max_Pic_Year,max_Pic_Month,min_Pic_Month,max_Pic_Day,min_Pic_Day\
                ,max_Pic_Hour,min_Pic_Hour,min_Del_Year,max_Del_Year,max_Del_Month,min_Del_Month\
                ,max_Del_Day,min_Del_Day=self.max_min_determination()

        schedule=self.shceduling_computation(min_Pic_Year,max_Pic_Year,max_Pic_Month,min_Pic_Month,max_Pic_Day,min_Pic_Day\
                ,max_Pic_Hour,min_Pic_Hour,min_Del_Year,max_Del_Year,max_Del_Month,min_Del_Month\
                ,max_Del_Day,min_Del_Day)
        

        return schedule




#schedule_1=time_scheduling_function([2016],[11],[12],[7],[2018],[12],[10],[6])
#schedule_2=time_scheduling_function([2016],[11],[12],[12],[2016],[12],[10],[6])
#schedule_3=time_scheduling_function([2016],[11],[12],[12],[2016],[12],[10],[6])




#print(schedule_1.not_list_test_functions())

#print(schedule_2.run())
#print(schedule_3.run())





