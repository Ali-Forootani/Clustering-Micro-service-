
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


def many_to_many_clustering_without_time_window_function(geo_clus,veh_clus,pic_lon_lat_2,del_lon_lat_2):
    
    s_t=np.shape(pic_lon_lat_2)


    ##############
    ############## Location Clustering Pickups


    clustering_loc_pickup= KMeans(n_clusters=int(geo_clus), random_state=0).fit(pic_lon_lat_2)
    location_labels_pickup=np.array(clustering_loc_pickup.labels_)
    location_centers_pickup=clustering_loc_pickup.cluster_centers_
    location_labels_pickup=np.reshape(location_labels_pickup,(s_t[0],1))


    ##############
    ############## Location Clustering Deliveries


    clustering_loc_deliveries= KMeans(n_clusters=int(geo_clus), random_state=0).fit(del_lon_lat_2)
    location_labels_deliveries=np.array(clustering_loc_deliveries.labels_)
    location_centers_deliveries=clustering_loc_deliveries.cluster_centers_
    location_labels_deliveries=np.reshape(location_labels_deliveries,(s_t[0],1))



    pickup_deliveries_labels=np.hstack((location_labels_pickup,location_labels_deliveries))

    clustering_pickup_deliveries_labels=KMeans(n_clusters=int(geo_clus), random_state=0).fit(pickup_deliveries_labels)
    labels_pickup_deliveries=np.array(clustering_loc_pickup.labels_)
    centers_pickup_deliveries=clustering_pickup_deliveries_labels.cluster_centers_
    labels_pickup_deliveries=np.reshape(labels_pickup_deliveries,(s_t[0],1))

    #print("++++")
    #print(labels_pickup_deliveries)
    #print("++++")
    ###############
    ############### 


    ###############
    ############### Car Clustering
    
    #gen_clusters=np.hstack((location_labels,TW))
    #clustering_Vh= KMeans(n_clusters=int(veh_clus), random_state=0).fit(gen_clusters)
    #cars=np.array(clustering_Vh.labels_)

    cars, centroids_Vh = kmeans1d.cluster(labels_pickup_deliveries, veh_clus)

    #print(cars)
    
    ############## Plotting

    colors_1=(0,1,0)
    plt.figure(1, figsize=(8, 4), facecolor='w', edgecolor='k')
    plt.scatter(pic_lon_lat_2[:,0], pic_lon_lat_2[:,1], c=colors_1, alpha=0.5)
    plt.scatter(del_lon_lat_2[:,0], del_lon_lat_2[:,1], c=(1,0,0), alpha=0.5)
    plt.title('2-D random geolocations')
    plt.xlabel('Geolocation many to many pickup-delivery')
    plt.ylabel('Geolocation many to many pickup-delivery')
    plt.scatter(location_centers_pickup[:,0],location_centers_pickup[:,1],marker='^')
    plt.scatter(location_centers_deliveries[:,0],location_centers_deliveries[:,1],marker='+')
    plt.show()




    return labels_pickup_deliveries, cars

