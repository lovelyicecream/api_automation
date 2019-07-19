# -*- coding:utf-8 -*-
from common.operate import get_path
from testcases.test_listpassenger import TestListPassenger
from testcases.test_listmeal import TestListMeal
from testcases.test_getmeal import TestGetMeal
from testcases.test_createorder import TestCreateOrder
from common.HTMLTestRunner import HTMLTestRunner
import unittest


def add_case(class_name):
    """
    add case by ClassName
    :param class_name:  ClassName from test module
    :return:
    """
    case = unittest.TestLoader().loadTestsFromTestCase(class_name)
    return case


if __name__ == '__main__':
    cases_list = [TestListPassenger, TestListMeal, TestGetMeal, TestCreateOrder]
    suites = unittest.TestSuite([add_case(case) for case in cases_list])
    html_path = get_path('reports', 'report.html')
    with open(html_path, 'wb') as fp:
        HTMLTestRunner(stream=fp,
                       title="ApiTest自动化测试报告",
                       description="用例执行结果:"
                       ).run(suites)
    fp.close()
