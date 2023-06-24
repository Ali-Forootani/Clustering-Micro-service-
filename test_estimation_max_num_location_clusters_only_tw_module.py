

import unittest
import numpy as np

from input_data_production import packet_list_creations
from input_data_production import input_data_processing

from estimation_max_num_location_clusters_only_tw_module import estimation_max_num_location_clusters_only_tw_function
from time_window_detection import time_window_seperation
from pre_processing_for_usecases_clustering_timewindow_module import pre_processing_for_usecases_clustering_timewindow_function
from time_computation_module import time_computation_function




def input_data_generation_for_testing_daily():
    
    num_samples=100

    packet_list_tw_daily,packet_list_without_tw_daily,packet_list_daily = packet_list_creations(int(num_samples),"Daily")
    pic_del_time_daily,schedule_daily,pic_pic_time_daily,del_del_time_daily = input_data_processing(packet_list_tw_daily,packet_list_without_tw_daily,packet_list_daily)

    return packet_list_tw_daily,packet_list_without_tw_daily,packet_list_daily,\
           pic_del_time_daily,schedule_daily
           




class Test_number_time_clust_only_tw_module(unittest.TestCase):

    def setUp(self):
        pass

    def test_estimation_max_num_location_clusters_only_tw_function(self):

        packet_list_tw_daily,packet_list_without_tw_daily,packet_list_daily,\
           pic_del_time_daily,schedule_daily = input_data_generation_for_testing_daily()
        processed_input_data_instance = time_window_seperation(packet_list_tw_daily)

        processed_input_data = processed_input_data_instance.run()

        print(processed_input_data[0])

        existance_time_window = "true"
        not_existance_time_window = "true"
        len_input_data = len(processed_input_data[0])
        pic_lon=processed_input_data[6]
        pic_lat=processed_input_data[7]
        del_lon=processed_input_data[3]
        del_lat=processed_input_data[4]
        Pic_Time=processed_input_data[22]

        print(len_input_data)

        pic_pic_time_instance = time_computation_function(Pic_Time,["Daily"],len_input_data)

        pic_pic_time_output = pic_pic_time_instance.run()

        print(pic_pic_time_output[0])

        #pic_lon, pic_lat, del_lon, del_lat, pic_lon_lat, del_lon_lat,pic_del_time=\
        #pre_processing_for_usecases_clustering_timewindow_function(existance_time_window,not_existance_time_window \
        #                                            ,pic_lon,pic_lat,del_lon,del_lat,len(Del_Hour),pic_pic_time,del_del_time)


        


    
    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
