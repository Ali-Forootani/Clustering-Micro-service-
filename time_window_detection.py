

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


import uuid
from random import randrange
from datetime import timedelta

###################
###################

class time_window_seperation:
    def __init__(self,packet_list):
        self.packet_list=packet_list


    def time_window_management(self):
        ids=[]
        TWs=[]
        Deliveries=[]
        Pick_ups=[]
    
        ids_2=[]
        Deliveries_2=[]
        Pick_ups_2=[]

        ###########

        del_lon=[]
        del_lat=[]

        pic_lon=[]
        pic_lat=[]

        del_lon_2=[]
        del_lat_2=[]

        pic_lon_2=[]
        pic_lat_2=[]

        time_wind_str=[]
        time_wind_end=[]

        Pic_Hour=[]
        Pic_Minute=[]
        Pic_Second=[]
        Pic_Year=[]
        Pic_Month=[]
        Pic_Day=[]

        Del_Hour=[]
        Del_Minute=[]
        Del_Second=[]
        Del_Year=[]
        Del_Month=[]
        Del_Day=[]
        Del_Time=[]
        Pic_Time=[]
        Del_Time=[]
    
        ######################
        ######################
        key_time="TW"

        j=0
        k=0


        for i in range(len(self.packet_list)):
        
            if key_time in self.packet_list[i]:
                

                #Exceptions
                if self.packet_list[i]['delivery']['coordinates'][0]['lon']==None and self.packet_list[i]['delivery']['coordinates'][0]['lat']==None:
                    raise Exception("The input data i" + self.packet_list[i]['id'] + "has no delivery coordinate")
                    
                if self.packet_list[i]['pick_up']['coordinates'][0]['lon']==None and self.packet_list[i]['pick_up']['coordinates'][0]['lat']==None:
                    raise Exception("The input data i" + self.packet_list[i]['id'] + "has no pick_up coordinate")


                ids.append(self.packet_list[i]['id'])
                TWs.append(self.packet_list[i]['TW'])
                Deliveries.append(self.packet_list[i]['delivery'])
                del_lon.append(float(self.packet_list[i]['delivery']['coordinates'][0]['lon']))
                del_lat.append(float(self.packet_list[i]['delivery']['coordinates'][0]['lat']))
                Pick_ups.append(self.packet_list[i]['pick_up'])
                pic_lon.append(float(self.packet_list[i]['pick_up']['coordinates'][0]['lon']))
                pic_lat.append(float(self.packet_list[i]['pick_up']['coordinates'][0]['lat']))

                time_wind_str.append(datetime.strptime(self.packet_list[i]['TW']['TW_str'], '%Y-%m-%d %H:%M:%S'))
                time_wind_end.append(datetime.strptime(self.packet_list[i]['TW']['TW_end'], '%Y-%m-%d %H:%M:%S'))

                Pic_Year.append(float(time_wind_str[j].year))
                Pic_Month.append(float(time_wind_str[j].month))
                Pic_Day.append(float(time_wind_str[j].day))
                Pic_Hour.append(float(time_wind_str[j].hour))
                Pic_Minute.append(float(time_wind_str[j].minute))
                Pic_Second.append(float(time_wind_str[j].second))
                Del_Year.append(float(time_wind_end[j].year))
                Del_Month.append(float(time_wind_end[j].month))
                Del_Day.append(float(time_wind_end[j].day))
                Del_Hour.append(float(time_wind_end[j].hour))
                Del_Minute.append(float(time_wind_end[j].minute))
                Del_Second.append(float(time_wind_end[j].second))
                Pic_Time.append(time_wind_str[j])
                Del_Time.append(time_wind_end[j])
                existance_time_window="true"
                j=j+1
            else:

                if self.packet_list[i]['delivery']['coordinates'][0]['lon']==None and self.packet_list[i]['delivery']['coordinates'][0]['lat']==None:
                    raise Exception("The input data i" + self.packet_list[i]['id'] + "has no delivery coordinate")
                    
                if self.packet_list[i]['pick_up']['coordinates'][0]['lon']==None and self.packet_list[i]['pick_up']['coordinates'][0]['lat']==None:
                    raise Exception("The input data i" + self.packet_list[i]['id'] + "has no pick_up coordinate")

                ids_2.append(self.packet_list[i]['id'])
                Deliveries_2.append(self.packet_list[i]['delivery'])
                del_lon_2.append(float(self.packet_list[i]['delivery']['coordinates'][0]['lon']))
                del_lat_2.append(float(self.packet_list[i]['delivery']['coordinates'][0]['lat']))
                Pick_ups_2.append(self.packet_list[i]['pick_up'])
                pic_lon_2.append(float(self.packet_list[i]['pick_up']['coordinates'][0]['lon']))
                pic_lat_2.append(float(self.packet_list[i]['pick_up']['coordinates'][0]['lat']))
                not_existance_time_window="true"
                k=k+1
        if k==0:
            not_existance_time_window="false"
        if j==0:
            existance_time_window="false"
            
    
        ######################
        ######################

        return ids,TWs,Deliveries,del_lon,del_lat,Pick_ups,pic_lon,pic_lat,time_wind_str,time_wind_end,Pic_Year,Pic_Month,Pic_Day,Pic_Hour \
               ,Pic_Minute,Pic_Second,Del_Year,Del_Month,Del_Day,Del_Hour,Del_Minute,Del_Second,Pic_Time,Del_Time,existance_time_window \
               ,ids_2,Deliveries_2,del_lon_2,del_lat_2,Pick_ups_2,pic_lon_2,pic_lat_2,not_existance_time_window

    def run(self):

        ids,TWs,Deliveries,del_lon,del_lat,Pick_ups,pic_lon,pic_lat,time_wind_str,time_wind_end,Pic_Year,Pic_Month,Pic_Day,Pic_Hour \
               ,Pic_Minute,Pic_Second,Del_Year,Del_Month,Del_Day,Del_Hour,Del_Minute,Del_Second,Pic_Time,Del_Time,existance_time_window \
               ,ids_2,Deliveries_2,del_lon_2,del_lat_2,Pick_ups_2,pic_lon_2,pic_lat_2,not_existance_time_window=self.time_window_management()
        #print(existance_time_window)

        return ids,TWs,Deliveries,del_lon,del_lat,Pick_ups,pic_lon,pic_lat,time_wind_str,time_wind_end,Pic_Year,Pic_Month,Pic_Day,Pic_Hour \
               ,Pic_Minute,Pic_Second,Del_Year,Del_Month,Del_Day,Del_Hour,Del_Minute,Del_Second,Pic_Time,Del_Time,existance_time_window \
               ,ids_2,Deliveries_2,del_lon_2,del_lat_2,Pick_ups_2,pic_lon_2,pic_lat_2,not_existance_time_window





###################
###################

