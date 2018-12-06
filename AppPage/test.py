# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 10:16
# @Author  : 清心
# @File    : test.py

import os
# import this
import string
import random
import collections
import time
import datetime
# from Base.startappium import StartApp


# driver = StartApp().get_driver()

# list = [1,2,3]
# b = ['orange','apple','bee','coca']
# for m,n in zip(list,b):
# 	if m == 3:
# 		print(n)
# 		# print("type(m):%s  type(n):%s   m:%s   n :%s" % (type(m), type(n), m, n))

#将嵌套的列表平铺打印出来
a = [[1,2,3],[4,5,6],[7,8,9]]
b =	[num for elem in a for num in elem]
print(b)

#打印当前目录下的所有 后缀为 .py 的文件
c = [filename for filename in os.listdir('.') if filename.endswith('.py')]
print(c)

#过滤大于0的数值
d = [-1,2,3,4,-2,-3,-6,25,-9,9,0]
e = [i for i in d if i>0]
print(e)


scores = {'hangSan':55 ,'wangWu':68 , 'liSi':86, 'xiaMing':59, 'liuNen':86}
height = max(scores.values())
low = min(scores.values())
avg = sum(scores.values())/len(scores)
heightPerson = [name for name, score in scores.items() if score == height]
print('height:%s\n low:%s\n avg:%s\n hp:%s' % (height,low,avg,heightPerson))

a = '08-08期：你好吗'
b = '你好'

if b in a: print('对的')
else: print('错的')

# 统计1000个字符串中出现次数最多的字符
x = string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
y = string.punctuation # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
z = string.digits # 0123456789
u = string.ascii_letters + string.digits + string.punctuation
m = [random.choice(u) for i in range(1000)]
print('m:%s' % m)
n = ''.join(m)
print('n:%s' % n)
d = collections.OrderedDict()
for ch in n:
	d[ch] = d.get(ch,0)+1
print(d)

mm = [1,2,3,4,5,6];q = ''
for i in range(6):q += '%s' % (mm[(-i)-1])
print('.'.join(q))
print(hash('.'.join(q)))

tm = time.strftime("%H:%M")
if tm > "15:00" and tm < "15:40":print(tm)
else:print("fffffffffff")

print(*range(4),4,*(5,6,7))

# 1. range()函数在python2*中返回的是一个包含若干整数的列表 ，在python3*中返回的是一个可迭代的对象
# 2.
mm0 = string.digits
rad = [random.choice(mm0) for i in range(1000)]
# 3.
bb = [0,1,2,3,4,5,6,7]

# aa = input("请输入取值范围，逗号分隔")
# # aa = eval(aa)
# if isinstance(aa, int) and 0 <= aa <= 100:
# 	aa += 1
# else:
# 	print("输入有误")

Today = datetime.date.today()
a = Today.timetuple().tm_yday
print("今天是今年中的第%s天,还有%s天过年" % (a,(365-a)))


def before_function(a_function):
	print("我是第一个方法哟")
	def inner_function():
		print("我在a_function方法的上方哟")
		a_function()
		print("我在a_function方法的下方哟")
	return inner_function

@before_function
def another_function():
	print("我是独立的方法哟")


print("-"*50)
another_function()
print("-"*50)


# 水仙花数   153  1**3 + 5**3 + 3**3 = 153 每个位置的立方和等于这个数的本身
for i in range(100,1000):
	ge = i%10
	shi = i // 10 % 10
	bai = i // 100
	if ge**3 + shi **3 + bai **3 == i:
		print(i)

for i in range(1,10):
	for j in range(1,i+1):
		print(j,"*",i,"=",i*j,"\t",end="")
	print()


#鸡兔同笼的问题，共有30 只鸡兔，90条腿，问各有多少只鸡和兔
for i in range(1,31):
	if i*2 + (30-i)*4 == 90:
		print(i)


#输出每个位数都不相同的数字
# dict = {1,2,3,4}
# for i in dict:
# 	for j in dict:
# 		for m in dict:
# 				if i != j and j != m and i != m:
# 					print(i*100+j*10+m)
#

x = []
while True:
	x.sort()
	if len(x) == 5:break
	m = random.randint(1,5)
	if m not in x:
		x.append(m)
print(x)



while True:
	for i in range(3):
		print(i)

	break


dic = [{"a":"1","b":"8","c":"3"},{"e":"2","c":"2","d":"3"},{"a":"2","e":"5","f":"2"}]

for i in dic:
	print("*"*50)
	print(i)



