#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Shawn'
__email__ = 'xxu@tenable.com'
__version__ = '0.2'

from tenable.sc import TenableSC
import getpass
from pprint import pprint
import time
import logging
#import requests
import json
#import yaml
#import base64
#import csv
#logging.basicConfig(level=logging.DEBUG)


sc = TenableSC("192.168.0.70")      # 替换SC地址
username = input('Input Username: ')  # 按提示输入用户名
password = getpass.getpass('Input Password: ')  # 按提示输入密码(密码不会显示在命令行输出)
sc.login(username, password)
'''
sc = TenableSC('192.168.0.70', access_key='8ace498eae084ce98e31097a5afb2fb5',
               secret_key='0eac5e94674d40ce88fe9217f812125b')
'''

'''
sc登录设置

sc = TenableSC("192.168.0.70")
sc.login('scan', '111')
'''

'''

plugins = sc.plugins.list(
    filter=('vprScore', 'gte', '9.9'), type='active', fields=['id', 'name', 'vprScore', 'vprContext']
)
# fields=['id', 'name', 'description', 'family', 'type', 'version', 'sourceFile', 'dependencies', 'cpe', 'protocol', 'riskFactor', 'solution', 'seeAlso', 'synopsis', 'checkType', 'exploitEase', 'exploitAvailable', 'exploitFrameworks', 'cvssVector', 'cvssVectorBF', 'baseScore', 'temporalScore', 'cvssV3Vector', 'cvssV3VectorBF', 'cvssV3BaseScore', 'cvssV3TemporalScore', 'vprScore', 'vprContext', 'stigSeverity', 'pluginPubDate', 'pluginModDate', 'patchPubDate', 'patchModDate', 'vulnPubDate', 'modifiedTime', 'md5', 'xrefs'
'''
cveid = input('Input CVE-ID: ')
plugins = sc.plugins.list(
    filter=('xrefs:CVE', 'like', cveid), type='active', fields=['id', 'name', 'checkType', 'vprScore', 'vprContext']
            )
for plugin in plugins:
    pprint(plugin)
    
sc.logout() #sc 登出
 
