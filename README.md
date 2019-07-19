Note:
 -  运行环境: windows10
 -  代码目前支持python3, 已通过Python 3.6.5下运行测试

Info:
 - 测试框架基于requests + unittest + ddt + HTMLTestRunner

Construct:


				|-----  common        :  配置文件和公共函数
				|-----  interface     :  接口api
				|-----  logs          :  日志文件
	            ApiTest ----|-----  params        :  参数文件
				|-----  reports       :  测试报告
				|-----  testcases     :  测试用例
