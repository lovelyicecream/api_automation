# -*- coding:utf-8 -*-

from common.config import create_source, create_skuStocks, create_createType
from common.config import create_buyerName, create_buyerPhone, create_buyerFfpCard
from common.logger import Log
import requests
import json
import time
import os

logger = Log()


def send_request(interface, method, url, json_data, timeout=30):
    """
    generate request method by requests library
    :param interface:  testing interface name
    :param method:  HTTP method
    :param url:   test url
    :param json_data:  json data
    :param timeout:  max_time for request
    :return:  response
    """
    try:
        response = requests.request(method=method, url=url, json=json_data, timeout=timeout)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error("Interface: %s called error: %s" % (interface, response.status_code))
    except Exception as e:
        logger.error("Interface: %s called Exception: %s" % (interface, e))


def format_time(timestamp):
    """
    format timestamp to "%Y-%m-%d %H:%M:%S"
    :param timestamp: timestamp
    :return: "%Y-%m-%d %H:%M:%S"
    """
    time_array = time.localtime(timestamp / 1000)
    time_format = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return time_format


def get_path(dirname, filename):
    """
    get the file of abspath
    :param dirname: dir's name
    :param filename:  file's name
    :return:  the file of abspath
    """
    return os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), dirname),
                        filename)


def write_json(filename, write_data):
    """
    write json file to AptTest/params
    :param filename: json filename
    :param write_data: dict
    :return: None
    """
    content = json.dumps(write_data)
    file_path = get_path('params', filename)
    with open(file_path, 'w') as f:
        f.truncate()
        f.write(content)


def read_json(filename):
    """
    read json file from AptTest/params
    :param filename: json filename
    :return: dict
    """
    file_path = get_path('params', filename)
    with open(file_path, 'r') as f:
        content = json.loads(f.read())
    return content


def format_create_json():
    """
    generator interface "create" for paramValues
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
