import unittest
import time
import ddt
from selenium import webdriver
from url_datas.global_datas import base_url
# from op_datas.fqsp_input_datas import Fqsp_da as input_a
from op_datas import fqsp_input_datas as input_a
from PageObject.fqsp_page import Ob_cxfw_sq
from yusuan_datas.fqsp_data import Objectpage_datas_Dlfw as login_dingwei

# 发起索赔

@ddt.ddt
class Test_cxhfw(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(base_url)
        cls.lp = Ob_cxfw_sq(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()
        print("用例执行完成")


    def test_cxhfw_2(self):
        try:
            self.lp.cxhfw_func(input_a.sucess["user"], input_a.sucess["passwd"], input_a.sucess["yzm"],input_a.sucess["单号"],input_a.sucess["申请人"],input_a.sucess["联系电话"],
                               input_a.sucess["运单号"],input_a.sucess["快件内容"],input_a.sucess["索赔金额"])
            print("**********************")
            login_name = self.driver.find_element_by_xpath(login_dingwei.wdzh_an).text
            print(login_name)
            tsy_text = str("我的账户")
            self.assertEqual(login_name,tsy_text)

        except Exception as msg:
            print("断言失败！",msg)
            raise




    # @ddt.data(*input_a.wrong_data)
    # def test_cxhfw_1(self,datas):
    #     self.lp.cxhfw_func(datas["user"],datas["passwd"],datas["yzm"],datas["单号"],datas["申请人"],datas["联系电话"],
    #                        datas["运单号"],datas["快件内容"],datas["索赔金额"])

