# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 14:53
# @Author  : 清心
# @File    : test_cy.py

import unittest
import time
from AppPage.cyhq import CYPage
from AppPage.cyjp import cyjp
from Base.startappium import StartApp
from Base.logger import Logger
logger = Logger(logger='CyTest').getlog()
driver = StartApp().get_driver()
# ws?token=0000002f:1532403388:cef4a838189a443090d9b8b8c7e5b69b8abaf917
url = 'http://gw.yundzh.com/ws?token=0000002f:1532403388:cef4a838189a443090d9b8b8c7e5b69b8abaf917'


class CyTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls): pass
# cls.driver = StartApp().get_driver()
# logger.info("我在CyTest实例化: %s" % cls.driver)

	def setUp(self): pass

	def tearDown(self): pass

	@classmethod
	def tearDownClass(cls):
		driver.quit()
	@staticmethod
	def test_1_hang(self):
		time.sleep(8)
		# CYPage().click_hq_zixuan()
		# time.sleep(1)
		# print("*"*50)
		# a = CYPage().zixuan_list()
		# list_name = CYPage().zixuan_name_list(a)
		# time.sleep(1)
		# print("-"*20)
		# for i in list_name:
		# 	print(i)
		# 	driver.find_element_by_android_uiautomator("new UiSelector().text(\"%s\")" % i).click()
		# 	time.sleep(3)
		# 	CYPage().go_back()
		# 	logger.info("返回，点击的是%s" % i)
		# 	time.sleep(2)

		CYPage().click_hq_hushen()
		CYPage().hangq_shangzheng_click()
		time.sleep(3)
		CYPage().go_back()
		time.sleep(2)
		CYPage().hangq_shenzheng_click()
		time.sleep(3)
		CYPage().go_back()
		CYPage().hangq_chuangye_click()
		time.sleep(3)
		CYPage().go_back()
		time.sleep(1)
		CYPage().hangye_one_click()
		time.sleep(2)
		CYPage().go_back()
		CYPage().jiepan_click()
		time.sleep(1)
		CYPage().ketang_click()
		time.sleep(1)

		CYPage().jiepan_click()

	@staticmethod
	def test_2_jie(self):
		time.sleep(8)
		CYPage().jiepan_click()
		cyjp().zao_zhi_click_text()
		cyjp().is_jp_title("往期FM")
		CYPage().go_back()
		cyjp().zao_zhi_click_image()
		cyjp().is_jp_title("往期FM")
		CYPage().go_back()
		cyjp().zao_zhi_click_blank()
		cyjp().is_jp_title("往期FM")
		zzx = cyjp().get_zao_zhi_FM_list()
		driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % zzx[0]).click()
		zzx_list = cyjp().get_zao_zhi_list()
		print(zzx_list)
		try:
			if zzx_list[2].split(" ")[1] in zzx_list[15] or zzx_list[2].split(" ")[1] in zzx_list[16] or zzx_list[2].split(" ")[1] in zzx_list[17]:
				print("最新一期和点击进入最新一期一致√")
				logger.info("最新一期和点击进入最新一期一致√")
			else:
				print("2:%s---\n  15:%s---\n  16:%s---\n  17:%s\n zzx_list:%s" % (zzx_list[2], zzx_list[15], zzx_list[16], zzx_list[17],zzx_list))
				logger.warning("2:%s---\n  15:%s---\n  16:%s---\n  17:%s\n zzx_list:%s" % (zzx_list[2], zzx_list[15], zzx_list[16], zzx_list[17],zzx_list))
		except Exception as e:
			print(e)
		CYPage().go_back()
		cyjp().zhi_bo_click_text()
		cyjp().is_jp_title("视频直播间")
		CYPage().go_back()
		cyjp().zhi_bo_click_image()
		cyjp().is_jp_title("视频直播间")
		CYPage().go_back()
		cyjp().zhi_bo_click_blank()
		cyjp().is_jp_title("视频直播间")
		CYPage().go_back()
		cyjp().guan_dian_click_text()
		cyjp().is_jp_title("观点直播")
		time.sleep(4)
		CYPage().go_back()
		cyjp().guan_dian_click_image()
		time.sleep(4)
		cyjp().is_jp_title("观点直播")
		CYPage().go_back()
		cyjp().guan_dian_click_blank()
		time.sleep(4)
		cyjp().is_jp_title("观点直播")
		CYPage().go_back()

	@staticmethod
	def test_3_ke(self):
		time.sleep(8)
		# self.driver.find_element_by_android_uiautomator('new UiSelector().text("自选")').click()
		driver.find_element_by_android_uiautomator('new UiSelector().text("课堂")').click()
		driver.find_element_by_android_uiautomator('new UiSelector().text("小白课堂")').click()
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().text("查看更多")').click()
		driver.press_keycode(4)
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().text("大咖来了")').click()
		time.sleep(2)
		driver.find_element_by_android_uiautomator('new UiSelector().text("查看更多")').click()
		driver.press_keycode(4)
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().text("实战课")').click()
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().text("查看更多")').click()
		driver.press_keycode(4)
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().text("理念课")').click()
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().text("查看更多")').click()
		driver.press_keycode(4)
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().text("选股")').click()
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().textContains("详情")').click()
		time.sleep(3)
		# self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("自选")').click()
		# time.sleep(2)
		driver.find_element_by_android_uiautomator('new UiSelector().text("分享")').click()
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().text("取消")').click()
		time.sleep(1)
		driver.press_keycode(4)
		driver.find_element_by_android_uiautomator('new UiSelector().text("股票池")').click()
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().textContains("详情")').click()
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().text("最新跟踪")').click()
		time.sleep(1)
		# self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("自选")').click()
		# time.sleep(2)
		# self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("自选")').click()
		driver.press_keycode(4)
		time.sleep(2)
		driver.find_element_by_android_uiautomator('new UiSelector().text("研报点金")').click()
		time.sleep(2)
		driver.find_element_by_android_uiautomator('new UiSelector().text("行情")').click()
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().textContains("自选")').click()
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().text("沪深")').click()
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().text("资讯")').click()
		time.sleep(1)
		driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()

	@staticmethod
	def test_4_mine(self):
		pass