from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from yusuan_datas.Op_datas import Objectpage_datas as loc
import time
from op_datas import login_datas as lodata


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def login_suc(self, user, passwd, yzm):
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(loc.index_loc)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(loc.dl_anniu)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(loc.user_loc)).send_keys(lodata.success['user'])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(loc.password_loc)).send_keys(lodata.success['passwd'])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(loc.yzm_loc)).send_keys(lodata.success['yzm'])
        self.driver.find_element_by_xpath(loc.login_button_loc).click()
        time.sleep(2) # 退出
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(loc.tc_an)).click()

    def login_er(self):

        self.driver.get_element_by_xpath(loc.login_err_loc)
        return self.driver.find_element_by_xpath(*loc.login_err_loc).text

