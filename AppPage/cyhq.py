# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 14:15
# @Author  : 清心
# @File    : cyhq.py

import unittest
from appium.webdriver.common.touch_action import TouchAction
from AppPage import xpath_adr
from Base.logger import Logger
from Base.startappium import StartApp

import time
logger = Logger(logger='CYPage').getlog()
driver = StartApp().get_driver()


class CYPage(object):

	# def __init__(self):
	# 	self.driver = StartApp().driver

	def get_size(self):
		x = driver.get_window_size()['width']
		y = driver.get_window_size()['height']
		return x, y

	def swipe(self, loc):
		if loc is 'l':
			self.to_right_swipe()
			logger.info('指针从左向右滑动')
		elif loc is 'r':
			self.to_left_swipe()
			logger.info('指针从右向左滑动')
		else:
			logger.info('输入错误，请输入 l or r')

	def to_left_swipe(self):
		l = self.get_size()
		return driver.swipe(l[0]*0.9, l[1]*0.5, l[0]*0.3, l[1]*0.5)

	def to_right_swipe(self):
		l = self.get_size()
		return driver.swipe(l[0]*0.3, l[1]*0.5, l[0]*0.9, l[1]*0.5)

	def click_hq_zixuan(self):
		"""点击自选按钮"""
		driver.find_element_by_android_uiautomator('new UiSelector().text("自选")').click()
		# TouchAction(self.driver).tap(x=367, y=128).perform()
		logger.info('点击行情页-自选')

	def click_hq_hushen(self):
		"""点击沪深按钮"""
		driver.find_element_by_android_uiautomator('new UiSelector().text("沪深")').click()
		logger.info('点击行情页-沪深')

	def click_hq_zixun(self):
		"""点击咨询按钮"""
		driver.find_element_by_android_uiautomator('new UiSelector().text("资讯")').click()
		logger.info('点击行情页-资讯')

	def go_back(self):
		"""坐标点击返回"""
		# [38, 97][60, 137]
		time.sleep(1)
		logger.info("等待2秒开始点击返回按钮")
		time.sleep(2)
		TouchAction(driver).tap(x=52, y=117).perform()
		time.sleep(2)

	def hangqing_click(self):
		"""点击底部行情导航栏"""
		logger.info('点击底部进入行情页')
		# TouchAction(self.driver).tap(x=180, y=1780).perform()
		driver.find_element_by_android_uiautomator('new UiSelector().text("行情")').click()

	def jiepan_click(self):
		"""点击底部直播导航栏"""
		logger.info('点击底部进入直播页')
		# TouchAction(self.driver).tap(x=530, y=1780).perform()
		driver.find_element_by_android_uiautomator('new UiSelector().text("解盘")').click()

	def ketang_click(self):
		"""点击底部课堂底部导航栏"""
		logger.info('点击底部进入课堂页')
		# TouchAction(self.driver).tap(x=900, y=1780).perform()
		driver.find_element_by_android_uiautomator('new UiSelector().text("课堂")').click()


	def hangq_shangzheng_click(self):
		"""点击行情-沪深模块的上证指数"""
		logger.info('点击上证指数')
		driver.find_element_by_android_uiautomator('new UiSelector().text("上证指数")').click()

	def hangq_shenzheng_click(self):
		logger.info('点击深证成指')
		driver.find_element_by_android_uiautomator('new UiSelector().text("深证成指")').click()

	def hangq_chuangye_click(self):
		logger.info('点击创业板指')
		driver.find_element_by_android_uiautomator('new UiSelector().text("创业板指")').click()

	def to_hangye_bankuai(self):
		"""点击行业板块的三角按钮"""
		logger.info('点击进入行业板块')
		# self.driver.find_element_by_xpath(xpath_adr.hangye_bankuai()).click()
		driver.find_element_by_android_uiautomator('new UiSelector().text("行业板块")').click()

	def hangye_one_click(self):
		logger.info('点击行业板块第一个对象')
		driver.find_element_by_xpath(xpath_adr.hangye_one()).click()

	def hangye_list(self):
		"""获取行业板块的列表信息"""
		logger.info('获取行业版块儿的列表信息')
		return driver.find_elements_by_xpath(xpath_adr.hangye_bankuai_list())

	def hangye_title(self):
		"""获取行业版块儿的标题"""
		logger.info('获取行业板块标题')
		return driver.find_elements_by_xpath(xpath_adr.hangye_bankuan_list_title())

	def hangye_back(self):
		"""返回行情页面"""
		logger.info('返回到行情页面')
		driver.find_element_by_xpath(xpath_adr.hangye_bankuai_back()).click()

	def zixuan_list(self):
		"""获取自选列表信息"""
		logger.info('获取行情页-自选-列表信息')
		_list = driver.find_elements_by_class_name(xpath_adr.zixuan_list())
		return _list
		# return self.driver.find_elements_by_class_name("android.view.ViewGroup")

	def zixuan_name_list(self, *loc):
		"""只适用于自选列表的自选股名称---OK成功"""
		_list = []
		_list_name = loc
		_list2 = []
		# print(loc)
		for i in _list_name[0]:
			_list.append(i.get_attribute('text'))
		num = 7
		for n in range(len(_list)):
			try:
				if num >= 7 and num <= n - len(_list)%5:
					print('第%s个企业是 %s' % (num, _list[num]))
					_list2.append(_list[num])
					num += 5
			except Exception as e:
				logger.warning('数组越界了，但是不影响使用:错误日志\n%s\n' % e)
		return _list2


	def hushen_list(self):
		logger.info('获取行情页-沪深-列表信息')
		_list = driver.find_elements_by_class_name(xpath_adr.hushen_list())
		return _list

	def name_list(self, *loc):
		_list = loc
		_list_name = []
		for i in _list[0]:
			_list_name.append(i.get_attribute('text'))
		return _list_name
		# for n in range(len(_list_name)):pass






	# def get_text(self):
	# 	logger.info("获取对象信息，输出文本信息")
	# 	self.driver.find_elements_by_css_selector('#screenshotContainer > div > div > div > div > div > div:nth-child(33)')