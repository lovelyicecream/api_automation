# -*- coding:utf-8 -*-

import json
import time
from common.config import create_source, create_skuStocks, create_createType
from common.config import create_buyerName, create_buyerPhone, create_buyerFfpCard


def format_time(timestamp):
    """
    format timestamp to "%Y-%m-%d %H:%M:%S"
    :param timestamp: timestamp
    :return: "%Y-%m-%d %H:%M:%S"
    """
    time_array = time.localtime(timestamp / 1000)
    time_format = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return time_format


def write_json(filename, write_data):
    """
    write json file to AptTest/params
    :param filename: json filename
    :param write_data: dict
    :return: None
    """
    content = json.dumps(write_data)
    file_path = "../params/{}".format(filename)
    with open(file_path, 'w') as f:
        f.truncate()
        f.write(content)


def read_json(filename):
    """
    read json file from AptTest/params
    :param filename: json filename
    :return: dict
    """
    file_path = "../params/{}".format(filename)
    with open(file_path, 'r') as f:
        content = json.loads(f.read())
    return content


def format_create_json():
    """
    interface "create" for paramValues
    :return:  list[dict1, dict2, dict3 ...]
    """
    list_passenger = read_json('list_passenger.json')
    list_meal = read_json('list_meal.json')
    get_meal = []
    for item in read_json('get_meal.json'):
        del item['scheduled_dept_time']
        get_meal.append(item)

    for i in range(len(list_passenger)):
        list_passenger[i].update(list_meal[i])
        list_passenger[i].update(get_meal[i])
        list_passenger[i]["source"] = create_source
        list_passenger[i]["create_type"] = create_createType
        list_passenger[i]["sku_stocks"] = create_skuStocks
        list_passenger[i]["buyer_name"] = create_buyerName
        list_passenger[i]["buyer_phone"] = create_buyerPhone
        list_passenger[i]["buyer_ffpcard"] = create_buyerFfpCard
    return list_passenger
