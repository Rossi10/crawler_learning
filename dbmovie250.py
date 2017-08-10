#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

f= open(r'G:\advanced\Python\111crawler\dbmovie250.txt','w')

'''构造函数，打印每个页面里的电影的题目和评分'''
def get_attractions(url,data=None):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('div.hd > a > span:nth-of-type(1)')
    rating_nums = soup.select('div.star > span.rating_num')
    for title,rating_num in zip(titles,rating_nums):
        data = {
            'title':title.get_text(),
            'rating_num':rating_num.get_text(),
        }
        data_value = data.values()
        for i in data_value:
            f.write(i)
        f.write('\n')

urls =[ 'https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25) ]
for single_url in urls:
    get_attractions(single_url)
f.close()