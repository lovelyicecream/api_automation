# -*- coding:utf-8 -*-
import requests
from common.logger import Log
from common.config import url, registry, version, getMeal_interface, getMeal_method, getMeal_paramTypes
from common.config import listPassenger_interface, listPassenger_method, listPassenger_paramTypes
from common.config import listMeal_interface, listMeal_method, listMeal_paramTypes

logger = Log()


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
        try:
            response = requests.post(url=url, json=payload, timeout=30)
            if response.status_code == 200:
                return response.json()
            else:
                logger.error("Interface: list_passenger called error: %s" % response.status_code)
        except Exception as e:
            logger.error("list_passenger Exception: ", e)

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
        try:
            response = requests.post(url=url, json=payload, timeout=30)
            if response.status_code == 200:
                return response.json()
            else:
                logger.error("Interface: list_meal called error: %s" % response.status_code)
        except Exception as e:
            logger.error("list_meal Exception: ", e)

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
        try:
            response = requests.post(url=url, json=payload, timeout=30)
            if response.status_code == 200:
                return response.json()
            else:
                logger.error("Interface: get_meal called error: %s" % response.status_code)
        except Exception as e:
            logger.error("get_meal Exception: ", e)
