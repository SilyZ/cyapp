# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 10:39
# @Author  : 清心
# @File    : startappium.py

from appium import webdriver
import time
import configparser
from .logger import Logger
import os
from AppPage.common import singleton

logger = Logger(logger='StartApp').getlog()


@singleton
class StartApp(object):

	def __init__(self):
		config = configparser.ConfigParser()
		# 'E:\\ppro\\cyapp\\appinfo.ini'
		path = os.path.dirname(os.path.abspath('.'))  # 获取相对路径
		config.read(path + '/appinfo.ini')
		time.sleep(1)
		desired_caps = dict()
		desired_caps['deviceName'] = config.get("conf", 'deviceName')
		desired_caps['platformName'] = config.get("conf", 'platformName')
		desired_caps['platformVersion'] = config.get("conf", 'platformVersion')
		desired_caps['noReset'] = True
		desired_caps['udid'] = config.get("conf", 'udid')
		desired_caps['app'] = config.get("conf", 'app')
		# desired_caps['automationName'] = config.get('conf','automationName')
		logger.info('读取ini文件成功：%s' % config)
		logger.info('写入字典成功-：%s' % desired_caps)
		time.sleep(3)
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		logger.info("我在StartApp 运行:----%s" % self.driver)

	def get_driver(self):
		return self.driver