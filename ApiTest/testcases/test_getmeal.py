# -*- coding:utf-8 -*-

import unittest
from ddt import ddt, file_data
from common.operate import get_path
from interface.meal.ProductApi import ProductApi


@ddt
class TestGetMeal(unittest.TestCase):

    @file_data(get_path('params', 'get_meal.json'))
    def test_getMeal(self, sku_id, scheduled_dept_time):
        self.content = ProductApi.get_meal(sku_id, scheduled_dept_time)
        if self.content['data']:
            self.assertEqual(self.content['code'], "0")
            self.assertTrue(self.content['success'])
            self.assertTrue(self.content['data']['canOrder'], 1)

if __name__ == '__main__':
    unittest.main()
