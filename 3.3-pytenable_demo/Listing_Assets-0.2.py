#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Shawn'
__email__ = 'xxu@tenable.com'
__version__ = '0.2'

from tenable.sc import TenableSC
from pprint import pprint
import getpass
import logging

#logging.basicConfig(level=logging.DEBUG)


'''
sc登录设置
仅需替换SC地址 ==> TenableSC("192.168.0.51")
'''
sc = TenableSC("192.168.0.70")      # 替换SC地址
username = input('Input Username: ')      #按提示输入用户名
password = getpass.getpass('Input Password: ')  #按提示输入密码(密码不会显示在命令行输出)
sc.login(username, password)


#sc.login('scan', '111') #使用固定的用户名、密码



for tup in list(enumerate(sc.asset_lists.list(
        fields=['name', 'ipCount'])['usable'])):
     if int(tup[1]['ipCount']) != 0:
        print(tup)

asset_id = input("\n输入上表中的资产'id': ")

_ = input('是否打印Repo名称? [Y/N]')
if _.lower() == 'y':
      show_repo = True
elif _.lower() == 'true':
      show_repo = True
else:
      show_repo = False
'''
输出repo的示例如下：
repo: public-cloud-scan
27.115.42.168|
180.168.251.245|b2b.erp.bl.com
180.168.251.246|bljt.oa.bl.com
202.121.129.18|
202.121.129.211|try.sufe.edu.cn
202.121.129.241|
202.121.129.245|
202.121.138.39|
202.121.138.79|blj.shufe.edu.cn
202.121.142.130|
'''


#Fetch the vaules of each key: 'ipList'
for d in sc.asset_lists.details(asset_id, fields=['viewableIPs'])['viewableIPs']:
      if int(d['ipCount']) == 0:
            pass
      else:
            if show_repo:
                  print('repo:', d['repository']['name'])
            print(d['ipList'])

#logout
sc.logout()
