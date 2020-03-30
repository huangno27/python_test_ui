import unittest
import time
import ddt
from selenium import webdriver
from url_datas.global_datas import base_url
from op_datas.fwfw_input_data import Fw_da as sj
from PageObject.fwfw_page import Ob_fwff

# 服务范围测试

@ddt.ddt
class Test_mdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(base_url)
        cls.lp = Ob_fwff(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()
        print("用例执行完成")

    # 成功的用例
    def test_login_2_suc(self):
        self.lp.ffwf_func(sj.sucess["user"], sj.sucess["passwd"], sj.sucess["yzm"],sj.sucess["gj"],sj.sucess["yb"])
        time.sleep(3)
    # 断言 city 关联出来的是不是BEIJING

