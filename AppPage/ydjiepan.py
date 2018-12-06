# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 10:45:21
# @Author  : 清心
# @File    : ydjiepan.py
"""
    I love s. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from Base.startappium import StartApp
from AppPage.cyhq import CYPage
import time
from Base.logger import Logger
from AppPage.cyjp import cyjp

logger = Logger(logger='ydjiepan').getlog()


class ydjiepan(object):

	def __init__(self):
		self.driver = StartApp().driver

	def left_swipe_three(self):
		"""滑动三次，进入解盘页"""
		x = self.driver.get_window_size()['width']
		y = self.driver.get_window_size()['height']
		for i in range(3):
			self.driver.swipe(x * 0.9, y * 0.5, x * 0.3, y * 0.5)
			time.sleep(1.5)
		try:
			self.driver.find_element_by_android_uiautomator('new UiSelector().text("立即体验")').click()
			time.sleep(1)
			TouchAction(self.driver).tap(x=1006, y=111).perform()
		except NoSuchElementException as e: print("当前在首页，不在欢迎页。\n%s" % e)

	def click_zaozhixiao(self):
		"""点击早知晓的动作"""
		cyjp().zao_zhi_click_blank()
		CYPage().go_back()
		cyjp().zao_zhi_click_image()
		CYPage().go_back()
		cyjp().zao_zhi_click_text()
		CYPage().go_back()
		logger.info("断言------")

	def click_zhibo(self):
		"""点击直播间的动作"""
		cyjp().zhi_bo_click_image()
		CYPage().go_back()
		cyjp().get_zhi_bo_title()

	def get_zhi_bo_time(self):
		"""任何时间进入直播间对比状态断言"""
		tm = time.strftime("%H:%M")
		if tm >= "09:10" and tm <= "09:40" :
			stu = cyjp().get_class_status()
			if stu[0] == "直播中":
				logger.info("%s==%s" % (stu[0], "直播中"))
			else:
				logger.warning("F 实际状态为:%s" % stu[0])
			num = 1
			for i in stu:
				print("第%s个直播的状态为:%s" % (num,i))
				num+=1
		elif tm >= "11:10" and tm <= "11:40":
			stu = cyjp().get_class_status()
			if stu[1] == "直播中":
				logger.info("%s==%s" % (stu[1], "直播中"))
			else:
				logger.warning("F 实际状态为:%s" % stu[1])
			num = 1
			for i in stu:
				print("第%s个直播的状态为:%s" % (num, i))
				num += 1
		elif tm >= "15:00" and tm <= "15:15":
			stu = cyjp().get_class_status()
			if stu[2] == "直播中":
				logger.info("%s==%s" % (stu[2], "直播中"))
			else:
				logger.warning("F 实际状态为:%s" % stu[2])
			num = 1
			for i in stu:
				print("第%s个直播的状态为:%s" % (num, i))
				num += 1
		elif tm >= "19:30" and tm <= "20:15" :
			stu = cyjp().get_class_status()
			if stu[3] == "直播中":
				logger.info("%s==%s" % (stu[3], "直播中"))
			else:
				logger.warning("F 实际状态为:%s" % stu[3])
			num = 1
			for i in stu:
				print("第%s个直播的状态为:%s" % (num, i))
				num += 1
		else:
			logger.info("非直播时间,老师们正在备课")
			stu = cyjp().get_class_status()
			num = 1
			for i in stu:
				print("第%s个直播的状态为:%s" % (num, i))
				num += 1