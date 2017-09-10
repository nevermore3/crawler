#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-10 18:48:27
# @Author  : jmq (58863790@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests
from bs4 import BeautifulSoup
import re
import os
class doutuSpider(object):
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"}
    def get_url(self,url):
        data = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(data.content,'lxml')
        totals = soup.findAll("a", {"class": "list-group-item"})    
        for one in totals:            
            sub_url = one.get('href')            
            global path
            path = sub_url.split('/')[-1]
            if not os.path.exists(path):
                os.mkdir(path)
            try:
                self.get_img_url(sub_url)
            except:
                pass



    def get_img_url(self,url):
        data = requests.get(url,headers = self.headers)
        soup = BeautifulSoup(data.content, 'lxml')
        #print type(soup)
        #print soup.img
        #print soup.img.get('src')
        #totals = soup.find_all('div',{'class':'col-xs-12 col-sm-12 artile_des'})
        totals = soup.find_all('img')
        print len(totals)
        #totals = soup.find(temp=re.compile(r'<img src=(.*) alt'))
        print totals
        for one in totals:
        #for img in totals:
            img = one.find('img')
            print img
            try:
                sub_url = img.get('src')
            except:
                pass
            finally:
                urls = 'http:' + sub_url
            try:
                self.get_img(urls)
            except:
                pass



    def get_img(self,url):
        filename = url.split('/')[-1]
        global path
        img_path = path+'\\'+filename

        img = requests.get(url,headers=self.headers)
        try:
            with open(img_path,'wb') as f:
                f.write(img.content)
        except:
            pass
    def create(self):
        for count in range(1, 31):
            url = 'https://www.doutula.com/article/list/?page={}'.format(count)
            print '开始下载第{}页'.format(count)
            self.get_url(url)
if __name__ == '__main__':
    doutu = doutuSpider()
    #doutu.create()

    for i in range(1,2):
        url = 'https://www.doutula.com/article/list/?page={}'.format(i)
        doutu.get_url(url)

