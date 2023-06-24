import unittest
from scheduling_module import time_scheduling_function




class Test_time_scheduling_function(unittest.TestCase):
    
    def setUp(self):
        pass
        
    
    def test_Yearly(self):

        schedule=time_scheduling_function([2016],[11],[12],[7],[2018],[12],[10],[6])
        
        self.assertEqual(schedule.run(), ["Yearly"])
        # check if numbers is instance of list
        #result = isinstance(2, list)
        #print(result)
        # Pic_Year,Pic_Month,Pic_Day,Pic_Hour,Del_Year,Del_Month,Del_Day,Del_Hour

    def test_Monthly(self):

        schedule=time_scheduling_function([2018],[11],[12],[7],[2018],[12],[10],[6])
        self.assertEqual(schedule.run(), ["Monthly"])
    def test_Weekly(self):
        schedule=time_scheduling_function([2018],[11],[11],[7],[2018],[11],[19],[6])
        self.assertEqual(schedule.run(), ["Weekly"])
    def test_Daily(self):
        schedule=time_scheduling_function([2018],[11],[12],[7],[2018],[11],[12],[9])
        self.assertEqual(schedule.run(), ["Daily"])

    def test_wrong_input_data_2(self):
        with self.assertRaises(Exception):
            schedule_2=time_scheduling_function(2018,[11],[11],[7],[2018],[11],[19],[6])
            schedule_2.not_list_test_functions()

    def test_worng_input_data_3(self):
        with self.assertRaises(Exception):
            schedule_3=time_scheduling_function([2018],11,[11],[7],[2018],[11],[19],[6])
            schedule_3.not_list_test_functions()

    def test_worng_input_data_4(self):
        with self.assertRaises(Exception):
            schedule_4=time_scheduling_function([2018],[11],11,[7],[2018],[11],[19],[6])
            schedule_4.not_list_test_functions()

    def test_worng_input_data_5(self):
        with self.assertRaises(Exception):
            schedule_5=time_scheduling_function([2018],[11],[11],7,[2018],[11],[19],[6])
            schedule_5.not_list_test_functions()

    def test_worng_input_data_6(self):
        with self.assertRaises(Exception):
            schedule_6=time_scheduling_function([2018],[11],[11],[7],2018,[11],[19],[6])
            schedule_6.not_list_test_functions()

    def test_worng_input_data_7(self):
        with self.assertRaises(Exception):
            schedule_7=time_scheduling_function([2018],[11],[11],[7],[2018],11,[19],[6])
            schedule_7.not_list_test_functions()

    def test_worng_input_data_8(self):
        with self.assertRaises(Exception):
            schedule_8=time_scheduling_function([2018],[11],[11],[7],[2018],[11],19,[6])
            schedule_8.not_list_test_functions()

    def test_worng_input_data_9(self):
        with self.assertRaises(Exception):
            schedule_9=time_scheduling_function([2018],[11],[11],[7],[2018],[11],[19],6)
            schedule_9.not_list_test_functions()

    def test_negative_input_data_1(self):
        with self.assertRaises(Exception):
            schedule_10=time_scheduling_function([-2018],[11],[11],[7],[2018],[11],[19],[6])
            schedule_10.negative_element_in_lists()

    def test_negative_input_data_2(self):
        with self.assertRaises(Exception):
            schedule_11=time_scheduling_function([2018],[-11],[11],[7],[2018],[11],[19],[6])
            schedule_11.negative_element_in_lists()

    def test_negative_input_data_3(self):
        with self.assertRaises(Exception):
            schedule_12=time_scheduling_function([2018],[11],[-11],[7],[2018],[11],[19],[6])
            schedule_12.negative_element_in_lists()

    def test_negative_input_data_4(self):
        with self.assertRaises(Exception):
            schedule_13=time_scheduling_function([2018],[11],[11],[-7],[2018],[11],[19],[6])
            schedule_13.negative_element_in_lists()

    def test_negative_input_data_5(self):
        with self.assertRaises(Exception):
            schedule_14=time_scheduling_function([2018],[11],[11],[7],[-2018],[11],[19],[6])
            schedule_14.negative_element_in_lists()

    def test_negative_input_data_6(self):
        with self.assertRaises(Exception):
            schedule_15=time_scheduling_function([2018],[11],[11],[7],[2018],[-11],[19],[6])
            schedule_15.negative_element_in_lists()

    def test_negative_input_data_7(self):
        with self.assertRaises(Exception):
            schedule_16=time_scheduling_function([2018],[11],[11],[7],[2018],[11],[-19],[6])
            schedule_16.negative_element_in_lists()

    def test_negative_input_data_8(self):
        with self.assertRaises(Exception):
            schedule_17=time_scheduling_function([2018],[11],[11],[7],[2018],[11],[19],[-6])
            schedule_17.negative_element_in_lists()
            #pass
            ##################################
            ##################################
            #schedule=time_scheduling_function([2018],[11],[11],[7],[2018],[11],[19],[6])
            #schedule=time_scheduling_function([2018],11,[11],[7],[2018],[11],[19],[6])
            #schedule=time_scheduling_function([2018],[11],11,[7],[2018],[11],[19],[6])
            #schedule=time_scheduling_function([2018],[11],[11],7,[2018],[11],[19],[6])
            #schedule=time_scheduling_function([2018],[11],[11],[7],2018,[11],[19],[6])
            #schedule=time_scheduling_function([2018],[11],[11],[7],[2018],11,[19],[6])
            #schedule=time_scheduling_function([2018],[11],[11],[7],[2018],[11],19,[6])
            #schedule=time_scheduling_function([2018],[11],[11],[7],[2018],[11],[19],6)
            #schedule=time_scheduling_function([2018],[11],[11],[7],[2017],[11],[19],[6])
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()