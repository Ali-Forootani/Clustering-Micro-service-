
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

#many_pickup_fixed_delivery_clustering_function


def fixed_pickup_many_delivery_clustering_function(time_clus,geo_clus,veh_clus,pic_del_time,del_lon_lat):
    
            s_t=np.shape(pic_del_time)

    
            ############# Time Clustering

            clustering_TW= KMeans(n_clusters=int(time_clus), random_state=0).fit(pic_del_time)
            centroids_TW= clustering_TW.cluster_centers_
            TW=np.array(clustering_TW.labels_)
            TW=np.reshape(TW,(s_t[0],1))
    
            ############# Location Clustering

            clustering_loc= KMeans(n_clusters=int(geo_clus), random_state=0).fit(del_lon_lat)
            location_labels=np.array(clustering_loc.labels_)
            location_centers=clustering_loc.cluster_centers_
            location_labels=np.reshape(location_labels,(s_t[0],1))

            ############# Car Clustering
    
            gen_clusters=np.hstack((location_labels,TW))
            clustering_Vh= KMeans(n_clusters=int(veh_clus), random_state=0).fit(gen_clusters)
            cars=np.array(clustering_Vh.labels_)


            ############## Plotting

            #colors_1=(0,1,0)
            #plt.figure(3, figsize=(8, 4), facecolor='w', edgecolor='k')
            #plt.scatter(del_lon_lat[:,0], del_lon_lat[:,1], c=colors_1, alpha=0.5)
            #plt.title('2-D random geolocations')
            #plt.xlabel('Geolocation fixed pickup-many delivery')
            #plt.ylabel('Geolocation fixed pickup-many delivery')
            #plt.scatter(location_centers[:,0],location_centers[:,1],c=(0,0,1))
            #plt.show()

            #print(location_centers)

            return TW,location_labels,cars

