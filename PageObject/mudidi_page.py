import time
from selenium import webdriver
from op_datas.mdd_input_data import Fwfw_dara as login_da
from yusuan_datas.mdd_datas import Objectpage_datas_mdd as login_dingwei
from selenium.webdriver.common.action_chains import ActionChains
from url_datas import global_datas






class Mdd_page:
#
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(global_datas.base_url)
        self.driver.maximize_window()


    def dw_jj(self,user,passwd,yzm,gj,gjz,ymsrk):
        time.sleep(2)
        self.driver.find_element_by_xpath(login_dingwei.index_loc).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(login_dingwei.dl_anniu).click()
        self.driver.find_element_by_xpath(login_dingwei.user_loc).send_keys(login_da.sucess['user'])
        self.driver.find_element_by_xpath(login_dingwei.password_loc).send_keys(login_da.sucess['passwd'])
        self.driver.find_element_by_xpath(login_dingwei.yzm_loc).send_keys(login_da.sucess['yzm'])
        time.sleep(2)
        self.driver.find_element_by_xpath(login_dingwei.login_button_loc).click()
        time.sleep(3)
        an = self.driver.find_element_by_xpath(login_dingwei.wyjj_loc)
        ActionChains(self.driver).move_to_element(an).perform()
        time.sleep(2)

        # 定位到目的地服务提示
        self.driver.find_element_by_xpath(login_dingwei.mdd_an).click()
        self.driver.find_element_by_xpath(login_dingwei.gjdq_an).send_keys(login_da.sucess['gj'])
        self.driver.find_element_by_xpath(login_dingwei.gjz_an).send_keys(login_da.sucess['gjz'])
        time.sleep(5)
        # 定位下载附件和分享按钮以及切换禁用品
        # 查询按钮,下载附件，分享按钮还不能用
        # self.driver.find_element_by_xpath(login_dingwei.cx_an).click()
        # self.driver.find_element_by_xpath(login_dingwei.xzfj_an).click()
        # self.driver.find_element_by_xpath(login_dingwei.fx_an).click()

        # 定位页码输入框输入数字跳转
        self.driver.find_element_by_xpath(login_dingwei.ymsrk_an).send_keys(login_da.sucess['ymsrk'])
        self.driver.find_element_by_xpath(login_dingwei.go_an).click()
        time.sleep(1)

        # self.driver.find_element_by_xpath(login_dingwei.syy_an).click()
        # # 定位禁运品
        # self.driver.find_element_by_xpath(login_dingwei.jyp_an).click()
        # self.driver.find_element_by_xpath()

