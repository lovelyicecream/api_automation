# -*- coding:utf-8 -*-

from common.config import url, registry, version, getMeal_interface, getMeal_method, getMeal_paramTypes
from common.config import listPassenger_interface, listPassenger_method, listPassenger_paramTypes
from common.config import listMeal_interface, listMeal_method, listMeal_paramTypes
from common.operate import send_request


class ProductApi(object):
    @staticmethod
    def list_passenger(id_card=None, id_type=None, tkne=None, passenger_name=None):
        payload = {
            "registry": registry,
            "interface": listPassenger_interface,
            "version": version,
            "method": listPassenger_method,
            "paramTypes": [listPassenger_paramTypes],
            "paramValues":
                [{"idCard": id_card, "idType": id_type, "tkne": tkne, "passengerName": passenger_name}]
        }
        return send_request('list_passenger', 'POST', url, json_data=payload)

    @staticmethod
    def list_meal(flight_no, scheduled_dept_time, orig, dest, seat_level):
        payload = {
            "registry": registry,
            "interface": listMeal_interface,
            "version": version,
            "method": listMeal_method,
            "paramTypes": [listMeal_paramTypes],
            "paramValues":
                [{"flightNo": flight_no, "scheduledDeptTime": scheduled_dept_time, "orig": orig, "dest": dest,
                  "seatLevel": seat_level}]
        }
        return send_request('list_meal', 'POST', url, json_data=payload)

    @staticmethod
    def get_meal(sku_id, scheduled_dept_time):
        payload = {
            "registry": registry,
            "interface": getMeal_interface,
            "version": version,
            "method": getMeal_method,
            "paramTypes": [getMeal_paramTypes],
            "paramValues":
                [{"skuId": sku_id, "scheduledDeptTime": scheduled_dept_time}]
        }
        return send_request('get_meal', 'POST', url, json_data=payload)
