# -*- coding: utf-8 -*-
# @Time    : 2018/7/23 11:41
# @Author  : 清心
# @File    : req.py

import requests
import json

url = 'http://gw.yundzh.com/ws?token=0000002f:1532403388:cef4a838189a443090d9b8b8c7e5b69b8abaf917'


headers={
	'Host' : 'gw.yundzh.com',
	'Upgrade' : 'websocket',
	'Connection' : 'Upgrade',
	'Sec-WebSocket-key' : '4+zLYuwVxGUhEOSAyd6/Gg==',
	'Sec-WebSocket-Version' : '13',
	'Accept-Encoding' : 'gzip',
	'User-Agent' : 'okhttp/3.6.0'
}

html = requests.get(url,headers=headers)
text = html.text
print(text)