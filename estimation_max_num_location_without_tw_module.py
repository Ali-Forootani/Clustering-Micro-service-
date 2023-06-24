
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




def estimation_max_num_location_clusters_without_tw_function(pic_lon_lat_2,del_lon_lat_2):
    
    s_t_2=np.shape(pic_lon_lat_2)

    ##########

    max_pickup_location_lon_2=np.max(pic_lon_lat_2[:,0])
    min_pickup_location_lon_2=np.min(pic_lon_lat_2[:,0])

    max_pickup_location_lat_2=np.max(pic_lon_lat_2[:,1])
    min_pickup_location_lat_2=np.min(pic_lon_lat_2[:,1])

    max_delivery_location_lon_2=np.max(del_lon_lat_2[:,0])
    min_delivery_location_lon_2=np.min(del_lon_lat_2[:,0])

    max_delivery_location_lat_2=np.max(del_lon_lat_2[:,1])
    min_delivery_location_lat_2=np.min(del_lon_lat_2[:,1])

    ##########
    
    glob_min_location_lon_2=float(min([min_pickup_location_lon_2,min_delivery_location_lon_2]))
    glob_max_location_lon_2=float(max([max_pickup_location_lon_2,max_delivery_location_lon_2]))


    glob_min_location_lat_2=float(min([min_pickup_location_lat_2,min_delivery_location_lat_2]))
    glob_max_location_lat_2=float(max([max_pickup_location_lat_2,max_delivery_location_lat_2]))
    
    ###########

    # one degree longitude = 111 km
    # one degree latitude = 111 km
    

    delta_lon_2=np.subtract(glob_max_location_lon_2,glob_min_location_lon_2)
    delta_lat_2=np.subtract(glob_max_location_lat_2,glob_min_location_lat_2)

    ave_packets_square_km=np.divide(int(st_2[0]),delta_lon_2*delta_lat_2*111)


    #print("******")
    #print(ave_packets_square_km)
    #print("******")

    max_num_location_clusters_without_tw=int(ave_packets_square_km*np.divide(delta_lon_2*delta_lat_2*111,25))

    return max_num_location_clusters_without_tw


