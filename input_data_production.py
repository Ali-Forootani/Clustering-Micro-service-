
import unittest
from time_window_detection import time_window_seperation

from datetime import datetime
import random

import uuid

from datetime import datetime
import random
from random import randrange
from datetime import timedelta

from time_window_detection import time_window_seperation
from time_computation_module import time_computation_function

from scheduling_module import time_scheduling_function

from pre_processing_for_usecases_clustering_module import pre_processing_for_usecases_clustering_function
from pre_processing_for_usecases_clustering_without_timewindow_module import pre_processing_for_usecases_clustering_without_timewindow_function

from estimation_max_num_time_clusters_module import estimation_max_num_time_clusters_function




def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    x=start + timedelta(seconds=random_second)
    return x


def packet_list_creations(num_samples,desired_schedule):

    # for Germany longitude: 5.93-15
    # for Germany latitude: 47.28-54.9

    packet_list_tw=[]
    packet_list_without_tw=[]
    packet_list=[]


    i=1

    if desired_schedule == "Daily":
        d1 = datetime.strptime('1/1/2000 7:00 AM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('1/1/2000 10:00 AM', '%m/%d/%Y %I:%M %p')
        d3 = datetime.strptime('1/1/2000 2:00 PM', '%m/%d/%Y %I:%M %p')
        d4 = datetime.strptime('1/1/2000 6:00 PM', '%m/%d/%Y %I:%M %p')


    if desired_schedule == "Weekly":
        d1 = datetime.strptime('1/1/2000 7:00 AM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('1/1/2000 10:00 AM', '%m/%d/%Y %I:%M %p')
        d3 = datetime.strptime('1/7/2000 2:00 PM', '%m/%d/%Y %I:%M %p')
        d4 = datetime.strptime('1/8/2000 6:00 PM', '%m/%d/%Y %I:%M %p')

    if desired_schedule == "Monthly":
        d1 = datetime.strptime('1/1/2000 7:00 AM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('1/1/2000 10:00 AM', '%m/%d/%Y %I:%M %p')
        d3 = datetime.strptime('2/8/2000 2:00 PM', '%m/%d/%Y %I:%M %p')
        d4 = datetime.strptime('2/18/2000 6:00 PM', '%m/%d/%Y %I:%M %p')


    if desired_schedule == "Yearly":
        d1 = datetime.strptime('1/1/2000 7:00 AM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('1/1/2000 10:00 AM', '%m/%d/%Y %I:%M %p')
        d3 = datetime.strptime('2/8/2001 2:00 PM', '%m/%d/%Y %I:%M %p')
        d4 = datetime.strptime('2/18/2002 6:00 PM', '%m/%d/%Y %I:%M %p')

    while i <= num_samples:

        x= {"id":str(uuid.uuid4()),
            "pick_up":{"coordinates": [{"lon":str(round(random.uniform(5.93, 15), 8)),"lat":str(round(random.uniform(47.28, 54.9), 8))}]},
            "delivery":{"coordinates": [{"lon":str(round(random.uniform(5.93, 15), 8)),"lat":str(round(random.uniform(47.28, 54.9), 8))}]},
            "TW":{"TW_str":str(random_date(d1,d2)),"TW_end":str(random_date(d3,d4))}
            }
    
        x_1= {"id":str(uuid.uuid4()),
            "pick_up":{"coordinates": [{"lon":str(round(random.uniform(5.93, 15), 8)),"lat":str(round(random.uniform(47.28, 54.9), 8))}]},
            "delivery":{"coordinates": [{"lon":str(round(random.uniform(5.93, 15), 8)),"lat":str(round(random.uniform(47.28, 54.9), 8))}]}
            }

        packet_list_tw.append(x)
        packet_list_without_tw.append(x_1)
        packet_list.append(x)
        packet_list.append(x_1)
        i=i+1

        #print(x.TWs)



    return packet_list_tw,packet_list_without_tw,packet_list


def input_data_processing(packet_list_tw,packet_list_without_tw,packet_list):

        
        processed_data=time_window_seperation(packet_list)
        
        output=processed_data.run()

        ids=output[0]
        TWs=output[1]
        Deliveries=output[2]
        del_lon=output[3]
        del_lat=output[4]
        Pick_ups=output[5]
        pic_lon=output[6]
        pic_lat=output[7]
        time_wind_str=output[8]
        time_wind_end=output[9]
        Pic_Year=output[10]
        Pic_Month=output[11]
        Pic_Day=output[12]
        Pic_Hour=output[13]
        Pic_Minute=output[14]
        Pic_Second=output[15]
        Del_Year=output[16]
        Del_Month=output[17]
        Del_Day=output[18]
        Del_Hour=output[19]
        Del_Minute=output[20]
        Del_Second=output[21]
        Pic_Time=output[22]
        Del_Time=output[23]
        existance_time_window=output[24]
        ids_2=output[25]
        Deliveries_2=output[26]
        del_lon_2=output[27]
        del_lat_2=output[28]
        Pick_ups_2=output[29]
        pic_lon_2=output[30]
        pic_lat_2=output[31]
        not_existance_time_window=output[32]
        #ids,TWs,Deliveries,del_lon,del_lat,Pick_ups,pic_lon,pic_lat,time_wind_str,time_wind_end,Pic_Year,Pic_Month,Pic_Day,Pic_Hour \
        #       ,Pic_Minute,Pic_Second,Del_Year,Del_Month,Del_Day,Del_Hour,Del_Minute,Del_Second,Pic_Time,Del_Time,existance_time_window \
        #       ,ids_2,Deliveries_2,del_lon_2,del_lat_2,Pick_ups_2,pic_lon_2,pic_lat_2,not_existance_time_window=time_window_seperation(packet_list)

        
        if existance_time_window == "true":

            

            schedule_class_instance=time_scheduling_function(Pic_Year,Pic_Month,Pic_Day,Pic_Hour,Del_Year,Del_Month,Del_Day,Del_Hour)

            schedule=schedule_class_instance.run()

            

            ###### UTC computation module- computation of unique time point for each existing time window in the input data



            pic_pic_time_class_instance=time_computation_function(Pic_Time,schedule,len(Del_Hour))

            pic_pic_time=pic_pic_time_class_instance.run()

            del_del_time_class_instance=time_computation_function(Del_Time,schedule,len(Del_Hour))

            del_del_time=del_del_time_class_instance.run()

            #print(pic_pic_time)
            #print(del_del_time)


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



        return pic_del_time,schedule,pic_pic_time,del_del_time




if __name__ == "__main__":

    packet_list_tw,packet_list_without_tw,packet_list=packet_list_creations(int(500),"Yearly")

    #estimation_max_num_time_clusters_function

    pic_del_time,schedule,pic_pic_time,del_del_time = input_data_processing(packet_list_tw,packet_list_without_tw,packet_list)

    ##########################
    ##########################

    num_samples=500

    packet_list_tw_daily,packet_list_without_tw_daily,packet_list_daily=packet_list_creations(int(num_samples),"Daily")
    pic_del_time_daily,schedule_daily,pic_pic_time_daily,del_del_time_daily = input_data_processing(packet_list_tw_daily,packet_list_without_tw_daily,packet_list_daily)

    packet_list_tw_weekly,packet_list_without_tw_weekly,packet_list_weekly=packet_list_creations(int(num_samples),"Weekly")
    pic_del_time_weekly,schedule_weekly,pic_pic_time_weekly,del_del_time_weekly = input_data_processing(packet_list_tw_weekly,packet_list_without_tw_weekly,packet_list_weekly)

    packet_list_tw_monthly,packet_list_without_tw_monthly,packet_list_monthly=packet_list_creations(int(num_samples),"Monthly")
    pic_del_time_monthly,schedule_monthly,pic_pic_time_monthly,del_del_time_monthly = input_data_processing(packet_list_tw_monthly,packet_list_without_tw_monthly,packet_list_monthly)

    packet_list_tw_yearly,packet_list_without_tw_yearly,packet_list_yearly=packet_list_creations(int(num_samples),"Yearly")
    pic_del_time_yearly,schedule_yearly,pic_pic_time_yearly,del_del_time_yearly = input_data_processing(packet_list_tw_yearly,packet_list_without_tw_yearly,packet_list_yearly)


    ##########################
    ##########################

#   print(len(pic_del_time))
    print(schedule_daily)
    print(schedule_weekly)
    print(schedule_monthly)
    print(schedule_yearly)
    print(len(pic_pic_time_yearly))


    num_time_clusters_instance = estimation_max_num_time_clusters_function(pic_del_time,schedule)

    num_time_clusters = num_time_clusters_instance.run()

    print(num_time_clusters[0])
    print(num_time_clusters[1])
    print(num_time_clusters[2])
    #glob_min_tw,glob_max_tw,st,max_num_time_clusters

    #print(packet_list)


