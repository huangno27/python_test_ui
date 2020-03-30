import time
from op_datas.ryf_input_data import Ryf_dara as input_a
from yusuan_datas.ryf_data import Objectpage_datas_ryf as login_dingwei
from selenium.webdriver.common.action_chains import ActionChains
from url_datas import global_datas
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Ob_cxfw_ryf:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get(global_datas.base_url)
        self.driver.maximize_window()

    # 燃油费
    def ryf_func(self,user,passwd,yzm):
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.index_loc)).click()
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.dl_anniu)).click()
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.user_loc)).send_keys(input_a.sucess['user'])
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.password_loc)).send_keys(input_a.sucess['passwd'])
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.yzm_loc)).send_keys(input_a.sucess['yzm'])
        self.driver.find_element_by_xpath(login_dingwei.login_button_loc).click()
        # 鼠标悬浮选择
        time.sleep(3)
        an = self.driver.find_element_by_xpath(login_dingwei.wyjj_loc)
        ActionChains(self.driver).move_to_element(an).perform()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.syryf_an)).click()
