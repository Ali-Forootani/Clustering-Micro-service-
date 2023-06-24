
import unittest
from time_window_detection import time_window_seperation

from datetime import datetime
import random

import uuid

from datetime import datetime
import random
from random import randrange
from datetime import timedelta



def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    x=start + timedelta(seconds=random_second)
    return x


def packet_list_creations():

    # for Germany longitude: 5.93-15
    # for Germany latitude: 47.28-54.9

    packet_list_tw=[]
    packet_list_without_tw=[]

    d1 = datetime.strptime('1/1/2000 7:00 AM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2000 10:00 AM', '%m/%d/%Y %I:%M %p')
    d3 = datetime.strptime('1/8/2000 2:00 PM', '%m/%d/%Y %I:%M %p')
    d4 = datetime.strptime('1/12/2000 6:00 PM', '%m/%d/%Y %I:%M %p')

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

    return packet_list_tw,packet_list_without_tw

def defective_packet_list_creations():



    defect_packet_list_tw_del=[]
    defect_packet_list_without_tw_del=[]

    defect_packet_list_tw_pick_up=[]
    defect_packet_list_without_tw_pick_up=[]
    
    d1 = datetime.strptime('1/1/2000 7:00 AM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2000 10:00 AM', '%m/%d/%Y %I:%M %p')
    d3 = datetime.strptime('1/8/2000 2:00 PM', '%m/%d/%Y %I:%M %p')
    d4 = datetime.strptime('1/12/2000 6:00 PM', '%m/%d/%Y %I:%M %p')


    x= {"id":str(uuid.uuid4()),
            "pick_up":{"coordinates": [{"lon":str(round(random.uniform(5.93, 15), 8)),"lat":str(round(random.uniform(47.28, 54.9), 8))}]},
            "delivery":{"coordinates": [{"lon":None,"lat":None}]},
            "TW":{"TW_str":str(random_date(d1,d2)),"TW_end":str(random_date(d3,d4))}
            }
    
    x_1= {"id":str(uuid.uuid4()),
            "pick_up":{"coordinates": [{"lon":str(round(random.uniform(5.93, 15), 8)),"lat":str(round(random.uniform(47.28, 54.9), 8))}]},
            "delivery":{"coordinates": [{"lon":None,"lat":None}]}
            }

    defect_packet_list_tw_del.append(x)
    defect_packet_list_without_tw_del.append(x_1)

    
    x= {"id":str(uuid.uuid4()),
            "pick_up":{"coordinates": [{"lon":None,"lat":None}]},
            "delivery":{"coordinates": [{"lon":str(round(random.uniform(5.93, 15), 8)),"lat":str(round(random.uniform(47.28, 54.9), 8))}]},
            "TW":{"TW_str":str(random_date(d1,d2)),"TW_end":str(random_date(d3,d4))}
            }

    x_1= {"id":str(uuid.uuid4()),
            "pick_up":{"coordinates": [{"lon":None,"lat":None}]},
            "delivery":{"coordinates": [{"lon":str(round(random.uniform(5.93, 15), 8)),"lat":str(round(random.uniform(47.28, 54.9), 8))}]}
            }

    defect_packet_list_tw_pick_up.append(x)
    defect_packet_list_without_tw_pick_up.append(x_1)

    return defect_packet_list_tw_del,defect_packet_list_without_tw_del,defect_packet_list_tw_pick_up,defect_packet_list_without_tw_pick_up


class Test_time_window_seperation(unittest.TestCase):
    
    def setUp(self):
        pass

    # "time_window_seperation" function form "time_window_detection" module has many outputs but we need following outputs:
    # Element of 24 for "existance_time_window"
    # Element of 32 for "not_existance_time_window"
    

    def test_time_window_tw(self):
        
        packet_list_tw,packet_list_without_tw=packet_list_creations()
        inputdata=time_window_seperation(packet_list_tw)
        output=inputdata.run()

        self.assertEqual(output[24], "true")

    def test_time_window_without_tw(self):
        
        packet_list_tw,packet_list_without_tw=packet_list_creations()
        inputdata=time_window_seperation(packet_list_without_tw)
        output=inputdata.run()
        self.assertEqual(output[32], "true")

    def test_tw_defect_delivery(self):

        defect_packet_list_tw_del,defect_packet_list_without_tw_del\
            ,defect_packet_list_tw_pick_up,defect_packet_list_without_tw_pick_up=defective_packet_list_creations()

        with self.assertRaises(Exception):
            inputdata=time_window_seperation(defect_packet_list_tw_del)
            output=inputdata.run()

    def test_tw_defect_pick_up(self):

        defect_packet_list_tw_del,defect_packet_list_without_tw_del\
            ,defect_packet_list_tw_pick_up,defect_packet_list_without_tw_pick_up=defective_packet_list_creations()

        with self.assertRaises(Exception):
            inputdata=time_window_seperation(defect_packet_list_tw_pick_up)
            output=inputdata.run()
     
            
    def test_without_tw_defect_delivery(self):

        defect_packet_list_tw_del,defect_packet_list_without_tw_del\
            ,defect_packet_list_tw_pick_up,defect_packet_list_without_tw_pick_up=defective_packet_list_creations()

        with self.assertRaises(Exception):
            inputdata=time_window_seperation(defect_packet_list_without_tw_del)
            output=inputdata.run()
    
    def test_without_tw_defect_pick_up(self):

        defect_packet_list_tw_del,defect_packet_list_without_tw_del\
            ,defect_packet_list_tw_pick_up,defect_packet_list_without_tw_pick_up=defective_packet_list_creations()

        with self.assertRaises(Exception):
            inputdata=time_window_seperation(defect_packet_list_without_tw_pick_up)
            output=inputdata.run()

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()





