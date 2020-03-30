import unittest
import time
import ddt
from selenium import webdriver
from url_datas.global_datas import base_url
from op_datas.xykh_input_datas import Wycs_da as sj
from PageObject.xykh_page import Ob_cxfw_xykh

# 协议客户

@ddt.ddt
class Test_cxhfw(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(base_url)
        cls.lp = Ob_cxfw_xykh(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()
        print("用例执行完成")

    # 成功的用例
    def test_cxhfw_1_suc(self):
        self.lp.cxhfw_xykh(sj.sucess["user"], sj.sucess["passwd"], sj.sucess["yzm"],sj.sucess["ydh"],
                           sj.sucess["ksrq"],sj.sucess["jsrq"],sj.sucess["zh"],sj.sucess["zdlx"],
                           sj.sucess["yx"],sj.sucess["mc"],sj.sucess["zh1"],sj.sucess["zt1"],
                           sj.sucess["qx1"],sj.sucess["szdq1"],sj.sucess["szdq2"])
        time.sleep(3)
        # 断言
        # 定位退出按钮
