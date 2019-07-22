# -*- coding:utf-8 -*-

from redis import StrictRedis, ConnectionPool
import pymysql
from common.config import redis_host, redis_port, redis_password, redis_db_index
from common.config import mysql_host, mysql_port, mysql_user, mysql_password, mysql_db


class DataBase(object):
    @classmethod
    def __connect_redis(cls):
        try:
            pool = ConnectionPool(host=redis_host,
                                  port=int(redis_port),
                                  password=redis_password,
                                  db=redis_db_index)
            conn = StrictRedis(connection_pool=pool)
        except:
            raise "Failed to connect Redis server!"

        return conn

    @classmethod
    def get_redis_value(cls, key):
        conn = cls.__connect_redis()
        try:
            result = conn.get(key).decode('utf-8')
        except:
            raise "Failed to get value of '%s' from redis" % key

        return result

    @classmethod
    def delete_redis_key(cls, key):
        conn = cls.__connect_redis()
        if conn.exists(key):
            conn.delete(key)
        else:
            raise "Failed to delete keys from redis"

    @classmethod
    def __connect_mysql(cls):
        try:
            conn = pymysql.connect(host=mysql_host,
                                   port=int(mysql_port),
                                   user=mysql_user,
                                   password=mysql_password,
                                   database=mysql_db)
        except:
            raise "Failed to connect MySQL server!"

        return conn

    @classmethod
    def get_mysql_value(cls, script):
        conn = cls.__connect_mysql()
        curosr = conn.cursor()
        try:
            curosr.execute(script)
            result = curosr.fetchall()

            return result
        except:
            raise "Failed to excute MySQL script"
        finally:
            curosr.close()
            conn.close()

# TestFunction
# print(DataBase.get_redis_value('meal:mealFlight:CN7179PEKSYX:2019-07-20 07'))
# print(DataBase.get_mysql_value("SELECT VERSION();"))
