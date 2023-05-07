# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:33:43 2023

@author: User
"""

import requests

url = 'https://notify-api.line.me/api/notify'
token = 'OymCUGgD2eeyi0yfM6SstODA4GX9GGtgjX91SXiYfci'
headers = {
    'Authorization': 'Bearer ' + token    # 設定權杖
}
data = {
    'message':'測試一下！',
    'imageThumbnail':'https://steam.oxxostudio.tw/downlaod/python/line-notify-demo.png',
    'imageFullsize':'https://steam.oxxostudio.tw/downlaod/python/line-notify-demo.png'     # 設定要發送的訊息
}
data = requests.post(url, headers=headers, data=data)   # 使用 POST 方法