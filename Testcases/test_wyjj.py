import unittest
import time
import ddt
from selenium import webdriver
from url_datas.global_datas import base_url
from op_datas import wyjj_datas as woyao
from PageObject.woyao_jijian_page import Woyao_jj
from yusuan_datas.jijian_datas import Objectpage_datas_jijian as dad

#

@ddt.ddt
class Test_wyjj(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(base_url)
        cls.lp = Woyao_jj(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()
        print("用例执行完成")

    # 成功的用例
    def test_login_2_suc(self):
        self.lp.dw_jj(woyao.sucess["user"], woyao.sucess["passwd"], woyao.sucess["yzm"],woyao.sucess["ydh"],
                      woyao.sucess["gj"],woyao.sucess["city"],woyao.sucess["yb"],woyao.sucess["jz"],
                      woyao.sucess["sl"],woyao.sucess["zl1"],woyao.sucess["chang"],woyao.sucess["kuan"],
                      woyao.sucess["gao"],woyao.sucess["wjzl"])
        time.sleep(3)
        # 断言 定位代理按钮
        self.driver.find_element_by_xpath(dad.qt_an).click()



    # 异常的用例
    # @ddt.data(*woyao.wrong_datas)
    # def test_login_1_err(self,datas):
    #     time.sleep(3)
    #     self.lp.dw_jj(datas['user'], datas['passwd'], datas['yzm'],woyao.sucess["ydh"],
    #                   datas["gj"], datas["city"], datas["yb"], datas["jz"],
    #                   datas["sl"], datas["zl1"], datas["chang"], datas["kuan"],
    #                   datas["gao"], datas["zl2"]
    #                   )
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath(dad.qt_an).click()

