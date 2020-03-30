# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 16:27
# @Author  : Mat
# @Email   : mat_wu@163.com
# @File    : constants.py
# @Software: PyCharm

import os
# print("当前所在目录:", os.path.dirname(__file__)) # 当前文件路径
# print("上级目录:", os.path.abspath(os.path.dirname(__file__))) # 当前文件路径上级目录
# root_dir = os.path.abspath(os.path.dirname(__file__))
# cases_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data", "cases.xlsx")
# print(cases_dir)
print(os.path.abspath(__file__)) # 当前文件绝对路径
print(os.path.dirname(os.path.abspath(__file__))) # 文件的上一级目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cases_dir = os.path.join(base_dir, "data", "cases.xlsx")
global_file = os.path.join(base_dir, "config", "global.conf")
online_file = os.path.join(base_dir, "config", "online.conf")
test_file = os.path.join(base_dir, "config", "test.conf")

logs_file = os.path.join(base_dir, "logs", "api.log")
testcases_dir = os.path.join(base_dir, "testcases")
report_file = os.path.join(base_dir, "report","api.html")