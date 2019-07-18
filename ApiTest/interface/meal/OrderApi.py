# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
import requests
from common.logger import Log
from common.config import url, registry, version
from common.config import create_interface, create_method, create_paramTypes

logger = Log()


class OrderApi(object):
    @staticmethod
    def create_order(id_card, id_type, tkne, flight_no, scheduled_dept_time, orig, dest, seat_level, sku_id, source,
                     create_type, sku_stocks, buyer_name, buyer_phone, buyer_ffpcard):
        payload = {
            "registry": registry,
            "interface": create_interface,
            "version": version,
            "method": create_method,
            "paramTypes": [create_paramTypes],
            "paramValues":
                [{"idCard": id_card, "idType": id_type, "tkne": tkne, "flightNo": flight_no,
                  "scheduledDeptTime": scheduled_dept_time, "orig": orig, "dest": dest, "seatLevel": seat_level,
                  "skuIds": [sku_id], "source": source, "createType": create_type, "skuStocks": [sku_stocks],
                  "buyerName": buyer_name, "buyerPhone": buyer_phone, "buyerFfpCard": buyer_ffpcard
                  }]
        }
        try:
            response = requests.post(url=url, json=payload, timeout=30)
            if response.status_code == 200:
                return response.json()
            else:
                logger.error("Interface: create_order called error: %s" % response.status_code)
        except Exception as e:
            logger.error("create_order Exception: ", e)
