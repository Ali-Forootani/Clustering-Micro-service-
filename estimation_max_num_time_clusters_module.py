

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



#################
#################
#################



class estimation_max_num_time_clusters_function:
    def __init__(self,pic_del_time,schedule):
        self.pic_del_time=pic_del_time
        self.schedule=schedule[0]

    def time_processing_function(self):
        
        st=np.shape(self.pic_del_time)

        max_pickup_time=np.max(self.pic_del_time[:,0])
        min_pickup_time=np.min(self.pic_del_time[:,0])
        ave_pickup_time=np.mean(self.pic_del_time[:,0])

        max_delivery_time=np.max(self.pic_del_time[:,1])
        min_delivery_time=np.min(self.pic_del_time[:,1])
        ave_delivery_time=np.mean(self.pic_del_time[:,1])

        glob_min_tw=float(min([max_pickup_time,min_pickup_time,max_delivery_time,min_delivery_time]))
        glob_max_tw=float(max([max_pickup_time,min_pickup_time,max_delivery_time,min_delivery_time]))

        return glob_min_tw,glob_max_tw,st,ave_delivery_time,ave_pickup_time,max_delivery_time,min_pickup_time
    
    def number_time_clust_based_on_schedule_daily(self,glob_min_tw,glob_max_tw,st,ave_delivery_time,ave_pickup_time,max_delivery_time,min_pickup_time):

        routin="Daily"

        #print("we are here")
        # 30 stands for half an hour in minute
        time_slot_unit_daily=30
        if float(glob_max_tw)>float(glob_min_tw):
           ave_num_packet_time_horizon=np.divide(st[0],np.subtract(glob_max_tw,glob_min_tw))
           max_num_time_clusters=int(np.divide(np.subtract(glob_max_tw,glob_min_tw),float(time_slot_unit_daily)))
        else:
             raise Exception("time window mismatch- global max time window is less than global min time window")

        return max_num_time_clusters , routin

    def number_time_clust_based_on_schedule_weekly(self,glob_min_tw,glob_max_tw,st,ave_delivery_time,ave_pickup_time,max_delivery_time,min_pickup_time):

        routin="Weekly"

        if float(glob_max_tw)>float(glob_min_tw):
             # We need to find out how many days-night are between the max and min time window
             # 24 stands the number of hours in a day-night
             # 60 stands the number of minutes in an hour
             ave_num_packet_time_horizon=np.divide(int(st[0]),np.subtract(glob_max_tw,glob_min_tw))
             div_coef=int(np.divide(np.subtract(ave_delivery_time,ave_pickup_time),60))
             num_of_days=int(np.divide(np.subtract(max_delivery_time,min_pickup_time),24*60))
            
             #time_slot_unit_weekly=div_coef*2
             max_num_time_clusters=int(np.dot(num_of_days,20))

        else:
             raise Exception("time window mismatch- global max time window is less than global min time window")

        return max_num_time_clusters , routin

    def number_time_clust_based_on_schedule_monthly(self,glob_min_tw,glob_max_tw,st,ave_delivery_time,ave_pickup_time,max_delivery_time,min_pickup_time):

        routin="Monthly"

            #to be modified later, but we should think about leap year detection
        
        if float(glob_max_tw)>float(glob_min_tw):
            ave_num_packet_time_horizon=np.divide(int(st[0]),np.subtract(glob_max_tw,glob_min_tw))
            num_of_months=int(np.divide(np.subtract(max_delivery_time,min_pickup_time),30*24*60))
            num_of_days=int(np.divide(np.subtract(max_delivery_time,min_pickup_time),24*60))
            max_num_time_clusters=int(np.dot(num_of_days,20))
        else:
            raise Exception("time window mismatch- global max time window is less than global min time window")

        return max_num_time_clusters , routin

    def number_time_clust_based_on_schedule_yearly(self,glob_min_tw,glob_max_tw,st,ave_delivery_time,ave_pickup_time,max_delivery_time,min_pickup_time):

        routin="Yearly"

        # to be modified later on, but we should think about leap year detection

        if float(glob_max_tw)>float(glob_min_tw):
             ave_num_packet_time_horizon=np.divide(int(st[0]),np.subtract(glob_max_tw,glob_min_tw))
             num_of_months=int(np.divide(np.subtract(max_delivery_time,min_pickup_time),30*24*60))
             num_of_days=int(np.divide(np.subtract(max_delivery_time,min_pickup_time),24*60))
             max_num_time_clusters=int(np.dot(num_of_days,20))
        else:
             raise Exception("time window mismatch- global max time window is less than global min time window")
        
        return max_num_time_clusters , routin

    def run(self):

        if self.schedule == "Daily":
            glob_min_tw,glob_max_tw,st,ave_delivery_time,ave_pickup_time,max_delivery_time,min_pickup_time = self.time_processing_function()
            max_num_time_clusters,routin = self.number_time_clust_based_on_schedule_daily(glob_min_tw,glob_max_tw,st,ave_delivery_time,ave_pickup_time,max_delivery_time,min_pickup_time)


        if self.schedule == "Weekly":
            glob_min_tw,glob_max_tw,st,ave_delivery_time,ave_pickup_time,max_delivery_time,min_pickup_time = self.time_processing_function()
            max_num_time_clusters,routin = self.number_time_clust_based_on_schedule_weekly(glob_min_tw,glob_max_tw,st,ave_delivery_time,ave_pickup_time,max_delivery_time,min_pickup_time)

        
        if self.schedule == "Monthly":
            glob_min_tw,glob_max_tw,st,ave_delivery_time,ave_pickup_time,max_delivery_time,min_pickup_time = self.time_processing_function()
            max_num_time_clusters,routin = self.number_time_clust_based_on_schedule_monthly(glob_min_tw,glob_max_tw,st,ave_delivery_time,ave_pickup_time,max_delivery_time,min_pickup_time)

        if self.schedule == "Yearly":
            glob_min_tw,glob_max_tw,st,ave_delivery_time,ave_pickup_time,max_delivery_time,min_pickup_time = self.time_processing_function()
            max_num_time_clusters,routin = self.number_time_clust_based_on_schedule_yearly(glob_min_tw,glob_max_tw,st,ave_delivery_time,ave_pickup_time,max_delivery_time,min_pickup_time)


        return glob_min_tw , glob_max_tw , st , max_num_time_clusters, routin

#################
#################
#################

