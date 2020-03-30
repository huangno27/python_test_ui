import unittest
import time
import ddt
from selenium import webdriver
from url_datas.global_datas import base_url
from op_datas.ffwd_datas import Fwwd_da as sj
from PageObject.fwwd_page import Op_ffwd

# 服务网点

@ddt.ddt
class Test_mdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(base_url)
        cls.lp = Op_ffwd(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()
        print("用例执行完成")

    # 成功的用例
    def test_login_2_suc(self):
        self.lp.ffwd_page(sj.sucess["user"], sj.sucess["passwd"], sj.sucess["yzm"],sj.sucess["cs"],sj.sucess["qx"])
        time.sleep(3)
        # 断言
        # 定位退出按钮
        # self.driver.find_element_by_xpath(dad.tq_an).click()
