# -*- coding:utf-8 -*-

import unittest
from ddt import ddt, file_data
from common.operate_json import write_json, format_time
from interface.meal.ProductApi import ProductApi


@ddt
class TestListPassenger(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filename = "list_meal.json"
        global data
        data = []

    @file_data('../params/list_passenger.json')
    def test_listPassenger(self, id_card=None, id_type=None, tkne=None, passenger_name=None):
        self.content = ProductApi.list_passenger(id_card, id_type, tkne, passenger_name)
        params = {
                'flight_no': self.content['data'][0]['flight']['flightNo'],
                'scheduled_dept_time': format_time(self.content['data'][0]['flight']['scheduledDeptTime']),
                'orig': self.content['data'][0]['flight']['orig'],
                'dest': self.content['data'][0]['flight']['dest'],
                'seat_level': self.content['data'][0]['seatLevel'],
                # 'tkne': self.content['data'][0]['tkne'],
                # 'idType': self.content['data'][0]['idType'],
                # 'idCard': self.content['data'][0]['idCard']
                  }
        data.append(params)

        # self.assertEqual(self.content['code'], "0")
        # self.assertTrue(self.content['success'])
        # self.assertRegex(str(self.content['data']), "SPECIAL_MEAL")

    @classmethod
    def tearDownClass(cls):
        write_json('list_meal.json', write_data=data)

if __name__ == '__main__':
    unittest.main()
