# coding:utf-8

import os
import configparser


cur_path = os.path.dirname(os.path.realpath(__file__))
configparh = os.path.join(cur_path, "config.ini")
conf = configparser.ConfigParser()
conf.read(configparh, encoding='utf-8')

# 读取数据
smtp_server = conf.get('email', "smtp_server")
sender = conf.get('email', "sender")
psw = conf.get('email', "psw")
receiver = conf.get('email', "receiver")
port = conf.get('email', "port")

print(smtp_server,sender,psw,receiver,port)
