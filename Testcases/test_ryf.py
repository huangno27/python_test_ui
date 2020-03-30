import unittest
import time
import ddt
from selenium import webdriver
from url_datas.global_datas import base_url
from op_datas.ryf_input_data import Ryf_dara as sj
from PageObject.ryf_page import Ob_cxfw_ryf

# 燃油费

@ddt.ddt
class Test_mdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(base_url)
        cls.lp = Ob_cxfw_ryf(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()
        print("用例执行完成")

    # 成功的用例
    def test_login_2_suc(self):
        self.lp.ryf_func(sj.sucess["user"], sj.sucess["passwd"], sj.sucess["yzm"])
        time.sleep(3)
        # 断言 定位代理按钮


    # 异常的用例
    # @ddt.data(*sj.wrong_datas)
    # def test_login_1_err(self,datas):
    #     time.sleep(3)
    #     self.lp.dw_jj(datas["user"], datas["passwd"], datas["yzm"],datas["gj"],datas["gjz"],datas["ymsrk"])
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath(dad.qt_an).click()


