
import redis
import json
import random
from decimal import *
import math
from numba import cuda
from numba import jit
import time
import pandas as pd
import os
import glob
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
import seaborn as sns
from pandas import read_excel
import redis
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pickle
from time import sleep
import kafka
from kafka import KafkaProducer


from kafka import KafkaConsumer
from json import loads
from time import sleep

import redis
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pickle
from time import sleep

######################
######################
######## Importing modules in the directory

from time_window_detection import time_window_seperation
from scheduling_module import time_scheduling_function
from time_computation_module import time_computation_function
from many_pickup_fixed_delivery_clustering_module import many_pickup_fixed_delivery_clustering_function
from fixed_pickup_many_delivery_clustering_module import fixed_pickup_many_delivery_clustering_function
from many_to_many_clustering_without_time_window_module import many_to_many_clustering_without_time_window_function
from pre_processing_for_usecases_clustering_module import pre_processing_for_usecases_clustering_function
from pre_processing_for_usecases_clustering_timewindow_module import pre_processing_for_usecases_clustering_timewindow_function
from pre_processing_for_usecases_clustering_without_timewindow_module import pre_processing_for_usecases_clustering_without_timewindow_function
from many_to_many_clustering_with_time_window_module import many_to_many_clustering_with_time_window_function
from estimation_max_num_time_clusters_module import estimation_max_num_time_clusters_function
from estimation_max_num_location_clusters_only_tw_module import estimation_max_num_location_clusters_only_tw_function
from estimation_max_num_location_clusters_module import estimation_max_num_location_clusters_function


######################
######################

redis_host='localhost'
redis_port= 6379

r=redis.StrictRedis(host=redis_host,port=redis_port,decode_responses=True)

#packet_list=json.loads(r.get('1ab2'))
#packet_list=json.loads(r.get('2ab3'))



def process_packet_list(packet_list):

    ##################
    ##################
    ##################
    ###### Input data processing which are in the json format
    
    ids,TWs,Deliveries,del_lon,del_lat,Pick_ups,pic_lon,pic_lat,time_wind_str,time_wind_end,Pic_Year,Pic_Month,Pic_Day,Pic_Hour \
               ,Pic_Minute,Pic_Second,Del_Year,Del_Month,Del_Day,Del_Hour,Del_Minute,Del_Second,Pic_Time,Del_Time,existance_time_window \
               ,ids_2,Deliveries_2,del_lon_2,del_lat_2,Pick_ups_2,pic_lon_2,pic_lat_2,not_existance_time_window=time_window_seperation(packet_list)

    ##################
    ##################
    ##################
    ####### Time scheduling detection module- Yearly/Montly/Weekly/Daily

    if existance_time_window == "true":
        schedule=time_scheduling_function(Pic_Year,Pic_Month,Pic_Day,Pic_Hour,Del_Year,Del_Month,Del_Day,Del_Hour)

        ###### UTC computation module- computation of unique time point for each existing time window in the input data

        pic_pic_time=time_computation_function(Pic_Time,schedule,len(Del_Hour))
        del_del_time=time_computation_function(Del_Time,schedule,len(Del_Hour))
    

    ##################
    ##################
    ##################
    ####### Pre-processing for usecases clustering- should be decided later also

    if existance_time_window == "true" and not_existance_time_window == "true":

        pic_del_time, pic_lon, pic_lat, del_lon, del_lat, pic_lon_lat, del_lon_lat, pic_lon_2, pic_lat_2, del_lon_2, \
            del_lat_2, pic_lon_lat_2, del_lon_lat_2=pre_processing_for_usecases_clustering_function(existance_time_window,\
                        not_existance_time_window,pic_pic_time,del_del_time,len(Del_Hour),\
                        pic_lon,pic_lat,del_lon,del_lat,pic_lon_2,pic_lat_2,del_lon_2,del_lat_2,len(pic_lon_2))

    
    if existance_time_window == "false" and not_existance_time_window == "true":
        pic_lon_2, pic_lat_2, del_lon_2, del_lat_2, pic_lon_lat_2, del_lon_lat_2=\
        pre_processing_for_usecases_clustering_without_timewindow_function(existance_time_window,not_existance_time_window \
                                                    ,pic_lon_2,pic_lat_2,del_lon_2,del_lat_2,len(pic_lon_2))



    if existance_time_window == "true" and not_existance_time_window == "false":
        pic_lon, pic_lat, del_lon, del_lat, pic_lon_lat, del_lon_lat,pic_del_time=\
        pre_processing_for_usecases_clustering_timewindow_function(existance_time_window,not_existance_time_window \
                                                    ,pic_lon,pic_lat,del_lon,del_lat,len(Del_Hour),pic_pic_time,del_del_time)

    if existance_time_window == "false" and not_existance_time_window == "false":

        raise Exception("Sorry there is no inout data")


    ####################
    
    #time_clus=6
    #geo_clus=15
    veh_clus=10


    if existance_time_window == "true":
        glob_min_tw,glob_max_tw,time_clus=estimation_max_num_time_clusters_function(pic_del_time,schedule[0])
    
    if existance_time_window == "true" and not_existance_time_window == "true":
        geo_clus=estimation_max_num_location_clusters_function(pic_lon_lat,del_lon_lat,pic_lon_lat_2,del_lon_lat_2)

    if existance_time_window == "true" and not_existance_time_window == "false":
        geo_clus=estimation_max_num_location_clusters_only_tw_function(pic_lon_lat,del_lon_lat)

    if existance_time_window == "false" and not_existance_time_window == "true":
        geo_clus=estimation_max_num_location_clusters_without_tw_function(pic_lon_lat_2,del_lon_lat_2)
    
    ########

    #print("////////")
    #print(time_clus)
    #print(geo_clus)
    #print("////////")


    if existance_time_window == "true" and not_existance_time_window == "true":

        s_t=np.shape(Del_Hour)
        s_t_w=np.shape(pic_lon_lat_2)

        ###### Many_pickup_fixed_delivery_clustering with time window

        TW_many_p_f_d,location_labels_many_p_f_d,Cars_labels_many_p_f_d=\
            many_pickup_fixed_delivery_clustering_function(time_clus,geo_clus,veh_clus,pic_del_time,pic_lon_lat)

        ###### Fixed_pickup_many_delivery_clustering with time window
        
        TW_f_p_many_d,location_labels_f_p_many_d,Cars_labels_f_p_many_d=\
            fixed_pickup_many_delivery_clustering_function(time_clus,geo_clus,veh_clus,pic_del_time,pic_lon_lat)

        ###### Many_to_many_pickups_delivery

        labels_many_to_many_pickup_deliveries, Cars_labels_many_to_many_p_d=\
           many_to_many_clustering_without_time_window_function(geo_clus,veh_clus,pic_lon_lat_2,del_lon_lat_2)


        ###### Many_to_many_time_pickups_delivery

        labels_time_many_to_many_pickup_deliveries, Cars_labels_many_to_many_time_p_d=\
            many_to_many_clustering_with_time_window_function(time_clus,geo_clus,veh_clus,pic_lon_lat,del_lon_lat,pic_del_time)

    if existance_time_window == "false" and not_existance_time_window == "true":
        
        s_t_w=np.shape(pic_lon_lat_2)

        ###### Many_to_many_pickups_delivery

        labels_many_to_many_pickup_deliveries, Cars_labels_many_to_many_p_d=\
           many_to_many_clustering_without_time_window_function(geo_clus,veh_clus,pic_lon_lat_2,del_lon_lat_2)
    
    if existance_time_window == "true" and not_existance_time_window == "false":

        s_t=np.shape(Del_Hour)

        ###### Many_pickup_fixed_delivery_clustering with time window

        TW_many_p_f_d,location_labels_many_p_f_d,Cars_labels_many_p_f_d=\
            many_pickup_fixed_delivery_clustering_function(time_clus,geo_clus,veh_clus,pic_del_time,pic_lon_lat)

        ###### Fixed_pickup_many_delivery_clustering with time window
    
        TW_f_p_many_d,location_labels_f_p_many_d,Cars_labels_f_p_many_d=\
            fixed_pickup_many_delivery_clustering_function(time_clus,geo_clus,veh_clus,pic_del_time,pic_lon_lat)

        ###### Many_to_many_time_pickups_delivery

        labels_time_many_to_many_pickup_deliveries, Cars_labels_many_to_many_time_p_d=\
            many_to_many_clustering_with_time_window_function(time_clus,geo_clus,veh_clus,pic_lon_lat,del_lon_lat,pic_del_time)


        #print(Cars_labels)
        #print(np.transpose(labels_time_many_to_many_pickup_deliveries))
    
    ##################
    ##################
    ##################

    ##################
    ##################
    ##################
    
    i=0
    
    clust_id_labels_many_to_many_time_p_d=[]
    if existance_time_window=="true":
        while i < int(s_t[0]):        
            x= {"id":str(ids[i]),
                    "car_labels":str(Cars_labels_many_to_many_time_p_d[i])
                    } 
            clust_id_labels_many_to_many_time_p_d.append(x)

            i=i+1
    
        with open('clust_id_labels_many_to_many_time_p_d.json','w') as writejson:
            json.dump(clust_id_labels_many_to_many_time_p_d,writejson, sort_keys=True, indent=2, ensure_ascii=False)
    
        with open('clust_id_labels_many_to_many_time_p_d.json') as f:
            clust_id_labels_many_to_many_time_p_d = json.load(f)

        with open('clust_id_labels_many_to_many_time_p_d.json') as f:
            clust_id_labels_many_to_many_time_p_d = json.load(f)

        json_object = json.dumps(clust_id_labels_many_to_many_time_p_d)
        r.set('clust_id_labels_many_to_many_time_p_d', json_object)
    
        ################################
        ################################

    clust_id_labels_many_to_many_p_d=[]
    i=0
    if not_existance_time_window=="true":
        while i < int(s_t_w[0]):
        
            x= {"id":str(ids_2[i]),
                    "car_labels_time":str(Cars_labels_many_to_many_p_d[i])
                    } 
            clust_id_labels_many_to_many_p_d.append(x)

            i=i+1
    
        with open('clust_id_labels_many_to_many_p_d.json','w') as writejson:
            json.dump(clust_id_labels_many_to_many_p_d,writejson, sort_keys=True, indent=2, ensure_ascii=False)
    
    
        with open('clust_id_labels_many_to_many_p_d.json') as f:
            clust_id_labels_many_to_many_p_d = json.load(f)


        with open('clust_id_labels_many_to_many_p_d.json') as f:
            clust_id_labels_many_to_many_p_d = json.load(f)


        json_object = json.dumps(clust_id_labels_many_to_many_p_d)
        r.set('clust_id_labels_many_to_many_p_d', json_object)

    

    return clust_id_labels_many_to_many_time_p_d, ids




#if __name__ == "__main__":

    
#    packet_list=json.loads(r.get('1ab2'))
    #packet_list=[]

#    clustering_id_labels, ids=process_packet_list(packet_list)

    #print(len(ids))

#    packet_list=json.loads(r.get('2ab3'))

#    clustering_id_labels, ids=process_packet_list(packet_list)

    #print(len(ids))

    #print(ids)
#    print("how r u?")
