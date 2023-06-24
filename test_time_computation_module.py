
import unittest
import numpy as np


from input_data_production import packet_list_creations
from input_data_production import input_data_processing

from time_computation_module import time_computation_function

from time_window_detection import time_window_seperation


def input_data_generation_for_testing():
    
    num_samples=10

    packet_list_tw,packet_list_without_tw,packet_list = packet_list_creations(int(num_samples),"Monthly")
    pic_del_time,schedule,pic_pic_time,del_del_time = input_data_processing(packet_list_tw,packet_list_without_tw,packet_list)

    return packet_list_tw,packet_list_without_tw,packet_list,\
           pic_del_time,schedule,pic_pic_time,del_del_time





class Test_time_computation_leap_year(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_checking_leap_year(self):

        packet_list_tw,packet_list_without_tw,packet_list,\
           pic_del_time,schedule,pic_pic_time,del_del_time = input_data_generation_for_testing()

        input_data_instance = time_window_seperation(packet_list)
        processed_input_data = input_data_instance.run()
        Pic_Time=processed_input_data[22]
        Del_Time=processed_input_data[23]
        s_t=np.shape(Pic_Time)

        time_computation_instance = time_computation_function([Pic_Time[0]],schedule,1)        
        #time_computation_output=time_computation_instance.run()

        #Leap year checking
        checking_leap_year_method=time_computation_instance.CheckLeap(2000)
        checking_leap_year_method_2=time_computation_instance.CheckLeap(2001)


        self.assertEqual(checking_leap_year_method, "true")
        self.assertEqual(checking_leap_year_method_2, "false")


    def test_UTC_function(self):

        packet_list_tw,packet_list_without_tw,packet_list,\
           pic_del_time,schedule,pic_pic_time,del_del_time = input_data_generation_for_testing()

        input_data_instance = time_window_seperation(packet_list)
        processed_input_data = input_data_instance.run()
        Pic_Time=processed_input_data[22]
        Del_Time=processed_input_data[23]
        s_t=np.shape(Pic_Time)

        time_computation_instance = time_computation_function([Pic_Time[0]],schedule,1)        
        time_computation_output=time_computation_instance.run()
        
        time_computation_instance_2 = time_computation_function([Del_Time[0]],schedule,1)
        time_computation_output_2=time_computation_instance_2.run()

        # January and a leap year-Monthly
        UTC=int(Pic_Time[0].month)*31*24*60+int(Pic_Time[0].day)*24*60+int(Pic_Time[0].hour)*60+int(Pic_Time[0].minute)
        self.assertEqual(time_computation_output[0][0], UTC)

        # Feburary and a leap year-Monthly
        UTC_2=int(Del_Time[0].month)*29*24*60+int(Del_Time[0].day)*24*60+int(Del_Time[0].hour)*60+int(Del_Time[0].minute)
        self.assertEqual(time_computation_output_2[0][0], UTC_2)

        pass


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

