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

# 切换到项目根据目录
os.chdir('D:\developer\work\workspace\YiDongHuiLi_Zpdyf_Basic_backup')
pass
# 执行命令清理ant之前生成缓存
os.system('ant clean')