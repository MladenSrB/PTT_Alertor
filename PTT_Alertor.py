# -*- coding: utf-8 -*-

from turtle import ht
import requests
import pandas as pd
from bs4 import BeautifulSoup
import sqlite3

url = "https://www.ptt.cc/bbs/MacShop/index.html"

html_doc = requests.get(url)
html = html_doc.text
soup = BeautifulSoup(html_doc.text, "html.parser")

#使用者條件設定
kind = '販售'      #徵求＆販售
series = 'iphone' #系列
generation = '14' #世代
area = '台北'       #區域
status = '售出' or '已售'    #狀態

#檢查Request回傳Response值
if html_doc.status_code == 200:
    print('獲取狀態:' + '成功' + '[' + str(html_doc.status_code) + ']')
else:
    print('獲取狀態:' + '失敗' + '[' + str(html_doc.status_code) + ']')





def get_all_href(url):
    html_doc = requests.get(url)
    html = html_doc.text
    soup = BeautifulSoup(html_doc.text, "html.parser")
    article_title = soup.select('div.title') #選擇<a>下的 div class="title", 以獲取文章標題及超連結herf
    for item in article_title:
        title = item.text
        title_low = title.lower()
        link = item.select_one('a') #確保已刪文的文章不會傳回None
        #Select article title include
        if link and kind in title_low and series in title_low and generation in title_low and area in title_low and status not in title_low:
            #Reply message with LINE Notify API
            headers = {"Authorization": "Bearer " + "rDfDKKV88vK4TgjmFzayzLEI57mTwfCwmISPLyfOmIS",
            "Content-Type": "application/x-www-form-urlencoded"}

            params = {"message": "成功獲取/n" + title + url}
 
            r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
            print(r.status_code)  # send status code 200 if succeed


for page in range(1,20):
    html_doc = requests.get(url)
    html = html_doc.text
    soup = BeautifulSoup(html_doc.text, "html.parser")
    btn = soup.select('div.btn-group > a')
    prev_btn_href = btn[3]['href']
    prev_page_url = 'https://www.ptt.cc' + prev_btn_href
    url = prev_page_url
    get_all_href(url = url)   