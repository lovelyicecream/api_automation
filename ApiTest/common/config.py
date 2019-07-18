# -*- coding:utf-8 -*-

import configparser
import os


def load_config(filename):
    """
    read config.ini
    :param filename: config.ini
    :return: cfg
    """
    try:
        config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), filename))
        cfg = configparser.ConfigParser()
        cfg.read(config_path, encoding="utf-8")
    except Exception as e:
        print(e)
    return cfg


config_file = "config.ini"
config = load_config(config_file)

url = config['common']['url']
registry = config['common']['registry']
version = config['common']['version']
content_type = config['common']['content_type']

# interface ProductApi.listPassenger
listPassenger_interface = config['ProductApi-listPassenger']['interface']
listPassenger_method = config['ProductApi-listPassenger']['method']
listPassenger_paramTypes = config['ProductApi-listPassenger']['paramTypes']

# interface ProductApi.listMeal
listMeal_interface = config['ProductApi-listMeal']['interface']
listMeal_method = config['ProductApi-listMeal']['method']
listMeal_paramTypes = config['ProductApi-listMeal']['paramTypes']

# interface ProductApi.getMeal
getMeal_interface = config['ProductApi-getMeal']['interface']
getMeal_method = config['ProductApi-getMeal']['method']
getMeal_paramTypes = config['ProductApi-getMeal']['paramTypes']

# interface OrderApi.create
create_interface = config['OrderApi-create']['interface']
create_method = config['OrderApi-create']['method']
create_paramTypes = config['OrderApi-create']['paramTypes']
create_source = config['OrderApi-create']['source']
create_createType = config['OrderApi-create']['createType']
create_skuStocks = config['OrderApi-create']['skuStocks']
create_buyerName = config['OrderApi-create']['buyerName']
create_buyerPhone = config['OrderApi-create']['buyerPhone']
create_buyerFfpCard = config['OrderApi-create']['buyerFfpCard']
