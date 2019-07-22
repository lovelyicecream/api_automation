# -*- coding:utf-8 -*-

from common.config import url, registry, version
from common.config import create_interface, create_method, create_paramTypes
from common.operate import send_request


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
        return send_request('create_order', 'POST', url, json_data=payload)
