import unittest
import time
import ddt
from selenium import webdriver
from url_datas.global_datas import base_url
from op_datas.mdd_input_data import Fwfw_dara as sj
from PageObject.mudidi_page import Mdd_page
from yusuan_datas.jijian_datas import Objectpage_datas_jijian as dad

# 目的地

@ddt.ddt
class Test_mdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(base_url)
        cls.lp = Mdd_page(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()
        print("用例执行完成")

    # 成功的用例
    def test_login_2_suc(self):
        self.lp.dw_jj(sj.sucess["user"], sj.sucess["passwd"], sj.sucess["yzm"],sj.sucess["gj"],sj.sucess["gjz"],sj.sucess["ymsrk"])
        time.sleep(3)
        # 断言 定位代理按钮

        self.driver.find_element_by_xpath(dad.qt_an).click()


    # 异常的用例
    # @ddt.data(*sj.wrong_datas)
    # def test_login_1_err(self,datas):
    #     time.sleep(3)
    #     self.lp.dw_jj(datas["user"], datas["passwd"], datas["yzm"],datas["gj"],datas["gjz"],datas["ymsrk"])
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath(dad.qt_an).click()


