# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 9:37
# @Author  : 清心
# @File    : cyjp.py
import time

from appium.webdriver.common.touch_action import TouchAction
from Base.logger import Logger
from Base.startappium import StartApp
logger = Logger(logger='cyjp').getlog()
from AppPage import xpath_adr
driver = StartApp().get_driver()

class cyjp(object):
	"""所有使用坐标的点击，更换手机之后就不好用了，定位会定位到一些奇怪的地方"""
	# def __init__(self):
	# 	self.driver = StartApp().driver

	def zao_zhi_click_text(self):
		driver.find_element_by_android_uiautomator('new UiSelector().text("早知晓")').click()
		logger.info("点击-文本-早知晓")

	def zao_zhi_click_image(self):
		"""换手机就不行了"""
		TouchAction(driver).tap(x=59, y=228).perform()
		logger.info("点击-图片-早知晓")

	def zao_zhi_click_blank(self):
		"""换手机就不行了"""
		TouchAction(driver).tap(x=596, y=232).perform()
		logger.info("点击-空白-早知晓")

	def click_title(self,loc):
		driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % loc[0]).click()
		logger.info("点击-标题-%s" % loc[0])

	def zhi_bo_click_text(self):
		driver.find_element_by_android_uiautomator('new UiSelector().text("视频直播间")').click()
		logger.info("点击-文本-视频直播间")

	def zhi_bo_click_image(self):
		"""换手机就不行了"""
		TouchAction(driver).tap(x=56, y=609).perform()
		logger.info("点击-图片-视频直播间")

	def zhi_bo_click_blank(self):
		"""换手机就不行了"""
		TouchAction(driver).tap(x=544, y=603).perform()
		logger.info("点击-空白-视频直播间")

	def guan_dian_click_text(self):
		driver.find_element_by_android_uiautomator('new UiSelector().text("观点直播")').click()
		logger.info("点击-文本-观点直播")

	def guan_dian_click_image(self):
		"""换手机就不行了"""
		TouchAction(driver).tap(x=56, y=943).perform()
		logger.info("点击-图片-观点直播")

	def guan_dian_click_blank(self):
		"""换手机就不行了"""
		TouchAction(driver).tap(x=607, y=954).perform()
		logger.info("点击-空白-观点直播")

	def is_jp_title(self, loc):
		time.sleep(1)
		text = driver.find_element_by_class_name("android.widget.TextView").get_attribute("text")
		if loc == text:
			logger.info("进入的是%s页面" % loc)
		else:
			logger.warning("当前页面不是-%s-页面,而是:%s" % (loc, text))

	def get_zao_zhi_FM_list(self):
		_lists = []
		_list = driver.find_elements_by_class_name('android.widget.TextView')
		for i, m in zip(range(len(_list)), _list):
			if i <= 1:
				pass
			elif i % 4 == 2:
				logger.info("早知晓title为:%s" % m.get_attribute("text")) # 08-08期：一根阳线转变三观
				_lists.append(m.get_attribute("text"))
		return _lists

	def get_zao_zhi_list(self):
		_lists = []
		_list = driver.find_elements_by_class_name("android.widget.TextView")
		for i in _list:
			logger.info("-----------:%s" % i.get_attribute("text"))
			_lists.append(i.get_attribute("text"))
		return _lists

	def get_zhi_bo_title(self):
		"""titlelist[0] 为 老师名字
		   titlelist[1] 为 直播标题
		"""
		titlelist = []
		name = driver.find_element_by_xpath(xpath_adr.zhi_bo_laoshi())
		title = driver.find_element_by_xpath(xpath_adr.zhi_bo_title())
		titlelist.append(name.split(" ")[0].split("老师")[0])# 将***老师 拆分放进集合
		titlelist.append(title)
		return titlelist

	def get_class_status(self):
		"""做断言用"""
		driver.find_element_by_android_uiautomator('new UiSelector().text("课程安排")').click()
		stus = []
		first_stus = driver.find_element_by_xpath(xpath_adr.zhi_bo_first_class_status()).get_attribute("text")
		stus.append(first_stus)
		second_stus = driver.find_element_by_xpath(xpath_adr.zhi_bo_second_class_status()).get_attribute("text")
		stus.append(second_stus)
		three_stus = driver.find_element_by_xpath(xpath_adr.zhi_bo_three_class_status()).get_attribute("text")
		four_stus = driver.find_element_by_xpath(xpath_adr.zhi_bo_four_class_status()).get_attribute("text")
		time.sleep(1)
		stus.append(three_stus)
		stus.append(four_stus)
		return stus

