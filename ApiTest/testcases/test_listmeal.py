# -*- coding:utf-8 -*-

import unittest
from ddt import ddt, file_data
from common.operate import write_json, get_path
from interface.meal.ProductApi import ProductApi


@ddt
class TestListMeal(unittest.TestCase):
    """
    test ProductApi.list_meal
    """
    @classmethod
    def setUpClass(cls):
        cls.filename = "get_meal.json"
        global data
        data = []

    @file_data(get_path('params', 'list_meal.json'))
    def test_listMeal(self, flight_no, scheduled_dept_time, orig, dest, seat_level):
        self.content = ProductApi.list_meal(flight_no, scheduled_dept_time, orig, dest, seat_level)
        if self.content['data']:
            params = {
                'sku_id': str(self.content['data'][0]['skuId']),
                'scheduled_dept_time': scheduled_dept_time
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
