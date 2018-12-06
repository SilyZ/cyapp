# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 17:51
# @Author  : 清心
# @File    : common.py

# 单例模式函数，用来修饰类


def singleton(cls, *args, **kw):  # cls是变量
    instances = {}  # 定义控制点

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton
