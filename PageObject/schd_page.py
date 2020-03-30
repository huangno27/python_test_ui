import time
from op_datas.schd_input_data import Wycs_da as input_a
from yusuan_datas.schd_data import Objectpage_datas_Schd as login_dingwei
from selenium.webdriver.common.action_chains import ActionChains
from url_datas import global_datas
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Ob_cxfw_one:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get(global_datas.base_url)
        self.driver.maximize_window()

    # 快件查询
    def cxhfw_func1(self,user,passwd,yzm):
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.index_loc)).click()
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.dl_anniu)).click()
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.user_loc)).send_keys(input_a.sucess['user'])
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.password_loc)).send_keys(input_a.sucess['passwd'])
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.yzm_loc)).send_keys(input_a.sucess['yzm'])
        self.driver.find_element_by_xpath(login_dingwei.login_button_loc).click()
        # 鼠标悬浮选择
        time.sleep(3)
        an = self.driver.find_element_by_xpath(login_dingwei.schd_an)
        ActionChains(self.driver).move_to_element(an).perform()
        # 点击促销信息
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.cxxx_an)).click()
        # 没有需要定位的元素
        # WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.cxxx_an)).click()
        # 定位每日抽奖
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.mrcj_an)).click()
        # 没有需要定位的元素
        # 定位大学快递
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.dxkd_an)).click()
        # 图片里的链接定位不到
        # 定位积分商城
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.jfsc_an)).click()


