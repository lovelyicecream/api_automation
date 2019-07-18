# -*- coding:utf-8 -*-

import unittest
from ddt import ddt, file_data
from interface.meal.ProductApi import ProductApi


@ddt
class TestGetMeal(unittest.TestCase):

    @file_data('../params/get_meal.json')
    def test_getMeal(self, sku_id, scheduled_dept_time):
        self.content = ProductApi.get_meal(sku_id, scheduled_dept_time)

        self.assertEqual(self.content['code'], "0")
        self.assertTrue(self.content['success'])
        self.assertTrue(self.content['data']['canOrder'], 1)

if __name__ == '__main__':
    unittest.main()
