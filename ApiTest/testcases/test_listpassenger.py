# -*- coding:utf-8 -*-

import unittest
from ddt import ddt, file_data
from common.operate import write_json, format_time, get_path
from interface.meal.ProductApi import ProductApi


@ddt
class TestListPassenger(unittest.TestCase):
    """
    test ProductApi.list_passenger
    """
    @classmethod
    def setUpClass(cls):
        cls.filename = "list_meal.json"
        global data
        data = []

    @file_data(get_path('params', 'list_passenger.json'))
    def test_listPassenger(self, id_card=None, id_type=None, tkne=None, passenger_name=None):
        self.content = ProductApi.list_passenger(id_card, id_type, tkne, passenger_name)
        if self.content['data']:
            params = {
                    'flight_no': self.content['data'][0]['flight']['flightNo'],
                    'scheduled_dept_time': format_time(self.content['data'][0]['flight']['scheduledDeptTime']),
                    'orig': self.content['data'][0]['flight']['orig'],
                    'dest': self.content['data'][0]['flight']['dest'],
                    'seat_level': self.content['data'][0]['seatLevel'],
                      }
            data.append(params)

            self.assertEqual(self.content['code'], "0")
            self.assertTrue(self.content['success'])
            self.assertRegex(str(self.content['data']), "SPECIAL_MEAL")

    @classmethod
    def tearDownClass(cls):
        write_json(cls.filename, write_data=data)

if __name__ == '__main__':
    unittest.main()
