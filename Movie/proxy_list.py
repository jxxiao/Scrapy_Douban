#coding:utf-8
import random
import scrapy
import logging
#ip代理的设置
class proxMiddleware(object):
    # def __init__(self):
    #     # self.file=open('reviewed_ips','r')
    #     self.proxy_list=[]
    #     # lines = self.file.readlines()
    #     for line in lines:
    #         self.proxy_list.append(line.strip('\n'))
    #     print self.proxy_list
    proxy_list=[

        '180.167.34.187:80',
        '101.53.101.172:9999',
        '183.78.183.156:82',
        '110.83.88.74:8118',
        '218.70.211.206:8118',
        '124.234.157.69:80',
        '171.13.37.203:808',
        '171.38.95.173:8123',
        '203.88.210.121:138',
        '171.38.129.105:8123'
    ]
    def process_request(self, request, spider):  #必须实现的方法
        # self.get_list_ips()
        request.meta['proxy']=random.choice(self.proxy_list)   #设置代理