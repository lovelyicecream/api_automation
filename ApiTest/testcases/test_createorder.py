# -*- coding:utf-8 -*-

import unittest
from ddt import ddt, file_data
from common.operate import format_create_json, write_json, get_path
from interface.meal.OrderApi import OrderApi


@ddt
class TestCreateOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        write_json(get_path('params', 'create_order.json'), format_create_json())

    @file_data(get_path('params', 'create_order.json'))
    def test_create_order(self, id_card, id_type, tkne, flight_no, scheduled_dept_time, orig, dest, seat_level, sku_id,
                          source, create_type, sku_stocks, buyer_name, buyer_phone, buyer_ffpcard):
        self.content = OrderApi.create_order(id_card, id_type, tkne, flight_no, scheduled_dept_time, orig, dest,
                                             seat_level, sku_id, source, create_type, sku_stocks, buyer_name,
                                             buyer_phone, buyer_ffpcard)

        if self.content:
            self.assertEqual(self.content['code'], "0")
            self.assertTrue(self.content['success'])
            self.assertRegex(str(self.content['data']), "SPECIAL_MEAL")

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
