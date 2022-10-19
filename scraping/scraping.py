import urllib.request as req 
import sys 
sys.path.append('/home/pi/.local/lib/python3.9/site-packages/') 
from bs4 import BeautifulSoup 
import csv

import numpy as np 
import pandas as pd

page = 10
year = 2022
month = 10

results = []

for n in range(page):
 url = "https://books.rakuten.co.jp/calendar/001020/monthly/?tid=" + str(year)+"-"+str(month).zfill(2)+"-01&p="+str(n+1) 
 res = req.urlopen(url) 
 soup = BeautifulSoup(res, "lxml") 
 item = soup(class_="item")

for m in range(len(item)):
 title = item[m](class_="item-title__text") 
 author = item[m](class_="item-author__name") 
 publisher = item[m](class_="item-publisher") 
 media=item[m](class_="item-title__media") 
 date = item[m](class_="item-release__date")

if len(title)==0:
    title = ""
else:
    title= title[0].text.replace('\u3000', ").replace('',") 
if len(author)==0:
    author = ""
else:
    author - author[0].text.replace('\u3000',").replace('', ") 
if len(publisher)==0:
    publisher = ""
else:
    publisher = publisher[0].text.replace('\u3000',").replace('',") 
if len(media)==0:
    media = ""
else:
    media = media[0].text.replace('\u3000',").replace('',").replace('(',").replace(')',") 
if len(date)==0:
    date = ""
else:
    date = date[0].text.replace('\n', ").replace('', ") 

results.append([date, title, author,media, publisher])
