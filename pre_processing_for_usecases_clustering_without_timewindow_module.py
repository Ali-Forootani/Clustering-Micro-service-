
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


####################
####################
####################

def pre_processing_for_usecases_clustering_without_timewindow_function(existance_time_window,not_existance_time_window \
                                                    ,pic_lon_2,pic_lat_2,del_lon_2,del_lat_2,len_pic_lon_2):

    
    if existance_time_window == "false" and not_existance_time_window == "true":

        pic_lon_2=np.reshape(pic_lon_2,(len(pic_lon_2),1))
        pic_lat_2=np.reshape(pic_lat_2,(len(pic_lon_2),1))
        del_lon_2=np.reshape(del_lon_2,(len(pic_lon_2),1))
        del_lat_2=np.reshape(del_lat_2,(len(pic_lon_2),1))

        pic_lon_lat_2=np.hstack((pic_lon_2,pic_lat_2))
        del_lon_lat_2=np.hstack((del_lon_2,del_lat_2))


    return pic_lon_2, pic_lat_2, del_lon_2, del_lat_2, pic_lon_lat_2, del_lon_lat_2

