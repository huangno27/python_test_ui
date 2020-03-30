import time
from selenium import webdriver
from op_datas.mdd_input_data import Fwfw_dara as login_da
from yusuan_datas.ryfjf_datas import Objectpage_datas_rfg as login_dingwei
from selenium.webdriver.common.action_chains import ActionChains
from url_datas import global_datas


class Op_ryf:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(global_datas.base_url)
        self.driver.maximize_window()


    def ryf_page(self, user, passwd, yzm):
        self.driver.find_element_by_xpath(login_dingwei.index_loc).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(login_dingwei.dl_anniu).click()
        self.driver.find_element_by_xpath(login_dingwei.user_loc).send_keys(login_da.sucess['user'])
        self.driver.find_element_by_xpath(login_dingwei.password_loc).send_keys(login_da.sucess['passwd'])
        self.driver.find_element_by_xpath(login_dingwei.yzm_loc).send_keys(login_da.sucess['yzm'])
        self.driver.find_element_by_xpath(login_dingwei.login_button_loc).click()
        time.sleep(3)

        an = self.driver.find_element_by_xpath(login_dingwei.wyjj_loc)
        ActionChains(self.driver).move_to_element(an).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath(login_dingwei.ryfjf_an).click()
        self.driver.find_element_by_xpath(login_dingwei.tq_an).click()

