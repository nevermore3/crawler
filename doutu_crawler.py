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
import urllib
global img_path 
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
            #path = sub_url.split('/')[-1]
            path = 'img'
            if not os.path.exists(path):
                os.mkdir(path)
            try:
                self.get_img_url(sub_url)
            except:
                pass

    def filter_url(self,url):
        Flag = False
        pattern = re.compile('(http.*\.jpg)',re.I)
        match = pattern.match(url)
        if  match:
            Flag = True
        return Flag

    def get_img_url(self,url):
        data = requests.get(url,headers = self.headers)
        soup = BeautifulSoup(data.content, 'lxml')
        totals = soup.find_all('img')        
        for one in totals:
            try:
                img_url  = one.attrs['src']               
                img_name = one.get('alt')              
                flag = self.filter_url(img_url)
                if img_name and flag:                  
                    self.get_img(img_name,img_url)
                else:
                    pass
            except:
                pass
 

    def get_img(self,name,url):
        print name +url
        global path
        img_path = path+'/'+name+'.jpg'
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
    doutu.create()
    #url = 'https://www.doutula.com/article/list/?page=2'
    #doutu.get_url(url)
    #for i in range(1,2):
    #    url = 'https://www.doutula.com/article/list/?page={}'.format(i)
    #    doutu.get_url(url)

