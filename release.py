# -*- coding: utf-8 -*-
import os
import sys
import requests


try:
  import configparser
except ImportError:
  import ConfigParser

try:
  cf = configparser.ConfigParser()
  print('python3')
except Exception as e:
  cf = ConfigParser.ConfigParser()
  print('python2')

os.chdir('D:\developer\work\workspace\YiDongHuiLi_Zpdyf_Basic_backup')
os.system('ant clean')
os.system('ant release')
# print(os.path)

# print(sys.path)

# filePath = os.path.dirname(__file__) + '/test'

# 读取配置文件
# cf.read(filePath)
# name = cf.get('app', 'sdk_dir')

# 网络请求
# response = requests.get("http://www.baidu.com")
# print(response.text)


