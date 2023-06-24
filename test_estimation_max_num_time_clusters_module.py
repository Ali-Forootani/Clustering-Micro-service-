
import unittest
import numpy as np

from input_data_production import packet_list_creations
from input_data_production import input_data_processing

from estimation_max_num_time_clusters_module import estimation_max_num_time_clusters_function
#from estimation_max_num_time_clusters_module import estimation_max_num_time_clusters_function




def input_data_generation_for_testing_daily():
    
    num_samples=500

    packet_list_tw_daily,packet_list_without_tw_daily,packet_list_daily = packet_list_creations(int(num_samples),"Daily")
    pic_del_time_daily,schedule_daily,pic_pic_time_daily,del_del_time_daily = input_data_processing(packet_list_tw_daily,packet_list_without_tw_daily,packet_list_daily)

    return packet_list_tw_daily,packet_list_without_tw_daily,packet_list_daily,\
           pic_del_time_daily,schedule_daily
           

def input_data_generation_for_testing_weekly():
    
    num_samples=500
    packet_list_tw_weekly,packet_list_without_tw_weekly,packet_list_weekly = packet_list_creations(int(num_samples),"Weekly")
    pic_del_time_weekly,schedule_weekly,pic_pic_time_weekly,del_del_time_weekly = input_data_processing(packet_list_tw_weekly,packet_list_without_tw_weekly,packet_list_weekly)

    return packet_list_tw_weekly,packet_list_without_tw_weekly,packet_list_weekly,\
           pic_del_time_weekly,schedule_weekly


def input_data_generation_for_testing_monthly():

    num_samples=500
    packet_list_tw_monthly,packet_list_without_tw_monthly,packet_list_monthly = packet_list_creations(int(num_samples),"Monthly")
    pic_del_time_monthly,schedule_monthly,pic_pic_time_monthly,del_del_time_monthly = input_data_processing(packet_list_tw_monthly,packet_list_without_tw_monthly,packet_list_monthly)

    return packet_list_tw_monthly,packet_list_without_tw_monthly,packet_list_monthly,\
           pic_del_time_monthly,schedule_monthly


def input_data_generation_for_testing_yearly():

    num_samples=500
    
    packet_list_tw_yearly,packet_list_without_tw_yearly,packet_list_yearly = packet_list_creations(int(num_samples),"Yearly")
    pic_del_time_yearly,schedule_yearly,pic_pic_time_yearly,del_del_time_yearly = input_data_processing(packet_list_tw_yearly,packet_list_without_tw_yearly,packet_list_yearly)

    return packet_list_tw_yearly,packet_list_without_tw_yearly,packet_list_yearly,\
           pic_del_time_yearly,schedule_yearly


def threshold_function(value_1,value_2):
    
    threshold=np.absolute(np.subtract(value_1,value_2))
    if  threshold <= 5:
        logic="true"
    else:
        logic="false"
    return logic





class Test_number_time_clust_based_on_schedule_daily(unittest.TestCase):

    def setUp(self):
        pass

    def test_num_time_clusters_daily(self):

        # We generate two set of different data and evaluate our algorithm, then we compare their results

        packet_list_tw_daily,packet_list_without_tw_daily,packet_list_daily,\
        pic_del_time_daily,schedule_daily = input_data_generation_for_testing_daily()

        packet_list_tw_daily_2,packet_list_without_tw_daily_2,packet_list_daily_2,\
        pic_del_time_daily_2,schedule_daily_2 = input_data_generation_for_testing_daily()

        num_time_clusters_instance = estimation_max_num_time_clusters_function(pic_del_time_daily,schedule_daily)
        num_time_clusters_instance_2 = estimation_max_num_time_clusters_function(pic_del_time_daily_2,schedule_daily_2)

        num_time_clusters = num_time_clusters_instance.run()
        num_time_clusters_2 = num_time_clusters_instance_2.run()

        # glob_min_tw , glob_max_tw , st , max_num_time_clusters, routin

        
        daily_logic=threshold_function(num_time_clusters[3],num_time_clusters_2[3])

        # Tests
        self.assertEqual(num_time_clusters[4], num_time_clusters_2[4])
        self.assertEqual(daily_logic, "true")

        print("1")


    def tearDown(self):
        pass



class Test_number_time_clust_based_on_schedule_weekly(unittest.TestCase):

    def setUp(self):
        pass


    def test_num_time_clusters_weekly(self):

        packet_list_tw_weekly,packet_list_without_tw_weekly,packet_list_weekly,\
        pic_del_time_weekly,schedule_weekly = input_data_generation_for_testing_weekly()

        packet_list_tw_weekly_2,packet_list_without_tw_weekly_2,packet_list_weekly_2,\
        pic_del_time_weekly_2,schedule_weekly_2 = input_data_generation_for_testing_weekly()

        num_time_clusters_instance = estimation_max_num_time_clusters_function(pic_del_time_weekly,schedule_weekly)
        num_time_clusters_instance_2 = estimation_max_num_time_clusters_function(pic_del_time_weekly_2,schedule_weekly_2)

        # glob_min_tw , glob_max_tw , st , max_num_time_clusters, routin

        num_time_clusters=num_time_clusters_instance.run()
        num_time_clusters_2=num_time_clusters_instance_2.run()

        self.assertEqual(num_time_clusters[4], "Weekly")
        self.assertEqual(num_time_clusters_2[4], "Weekly")

        weekly_logic=threshold_function(num_time_clusters[3],num_time_clusters_2[3])

        self.assertEqual(weekly_logic, "true")

        print("2")

    def tearDown(self):
        pass



class Test_number_time_clust_based_on_schedule_monthly(unittest.TestCase):

    def setUp(self):
        pass

    def test_num_time_clusters_monthly(self):

        packet_list_tw_monthly,packet_list_without_tw_monthly,packet_list_monthly,\
        pic_del_time_monthly,schedule_monthly = input_data_generation_for_testing_monthly()

        packet_list_tw_monthly_2,packet_list_without_tw_monthly_2,packet_list_monthly_2,\
        pic_del_time_monthly_2,schedule_monthly_2 = input_data_generation_for_testing_monthly()

        num_time_clusters_instance_monthly = estimation_max_num_time_clusters_function(pic_del_time_monthly,schedule_monthly)
        num_time_clusters_instance_monthly_2 = estimation_max_num_time_clusters_function(pic_del_time_monthly_2,schedule_monthly_2)

        num_time_clusters_monthly=num_time_clusters_instance_monthly.run()
        num_time_clusters_monthly_2=num_time_clusters_instance_monthly_2.run()

        self.assertEqual(num_time_clusters_monthly[4], "Monthly")
        self.assertEqual(num_time_clusters_monthly_2[4], "Monthly")

        monthly_logic=threshold_function(num_time_clusters_monthly[3],num_time_clusters_monthly_2[3])

        self.assertEqual(monthly_logic, "true")

        print("3")
        print("here I am")

    def tearDown(self):
        pass

class Test_number_time_clust_based_on_schedule_monthly(unittest.TestCase):

    def setUp(self):
        pass

    def test_num_time_clusters_yearly(self):

        packet_list_tw_yearly,packet_list_without_tw_yearly,packet_list_yearly,\
        pic_del_time_yearly,schedule_yearly = input_data_generation_for_testing_yearly()


        packet_list_tw_yearly_2,packet_list_without_tw_yearly_2,packet_list_yearly_2,\
        pic_del_time_yearly_2,schedule_yearly_2 = input_data_generation_for_testing_yearly()


        num_time_clusters_instance_yearly = estimation_max_num_time_clusters_function(pic_del_time_yearly,schedule_yearly)
        num_time_clusters_instance_yearly_2 = estimation_max_num_time_clusters_function(pic_del_time_yearly_2,schedule_yearly_2)


        num_time_clusters_yearly=num_time_clusters_instance_yearly.run()
        num_time_clusters_yearly_2=num_time_clusters_instance_yearly_2.run()
        self.assertEqual(num_time_clusters_yearly[4], "Yearly")
        self.assertEqual(num_time_clusters_yearly_2[4], "Yearly")

        yearly_logic=threshold_function(num_time_clusters_yearly[3],num_time_clusters_yearly_2[3])

        #self.assertEqual(yearly_logic, "true")

        print("4")

    def tearDown(self):
        pass





if __name__ == '__main__':
    unittest.main()
