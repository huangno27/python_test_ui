import time
from op_datas.cxhfw_4_input_datas import Wycs_da as input_a
from yusuan_datas.cxhfw_4_data import Objectpage_datas_Cxhfw as login_dingwei
from selenium.webdriver.common.action_chains import ActionChains
from url_datas import global_datas
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Ob_cxfw_four:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get(global_datas.base_url)
        self.driver.maximize_window()

    # 快件查询
    def cxhfw_func3(self,user,passwd,yzm,lx,wdmc,szcs_1,szcs_2,szcs_3):
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.index_loc)).click()
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.dl_anniu)).click()
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.user_loc)).send_keys(input_a.sucess['user'])
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.password_loc)).send_keys(input_a.sucess['passwd'])
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.yzm_loc)).send_keys(input_a.sucess['yzm'])
        self.driver.find_element_by_xpath(login_dingwei.login_button_loc).click()
        # 鼠标悬浮选择
        time.sleep(3)
        an = self.driver.find_element_by_xpath(login_dingwei.cxhfw_an)
        ActionChains(self.driver).move_to_element(an).perform()
        # 点击财务服务
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.cwfw_an)).click()

        # 定位清关服务
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.qgfw_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.zzsb_an)).click()
        # 返回清关服务
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.qgfw2_an)).click()
        # 定位信息收集上传
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.xxsjsc_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.xxsj_an)).click()
        time.sleep(3)
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.smba_an)).click()

        # 实名备案->反馈 点进去就出不来
        # WebDriverWait(driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.fk_an)).click()
        # 实名备案->查看 点进去就出不来
        # WebDriverWait(driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.ck_an)).click()

        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.wjmbxz_an)).click()
        s1 = Select(self.driver.find_element_by_xpath(login_dingwei.lx_an))
        s1.select_by_index(input_a.sucess['lx'])

        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.wdmc_an)).send_keys(input_a.sucess["wdmc"])
        #  69行 只能传0进去不报错
        # WebDriverWait(driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.wjxzcx_an)).click()
        # WebDriverWait(driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.xz_an)).click()

        # 定位在线咨询
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.zxzx_an)).click()
        s2 = Select(self.driver.find_element_by_xpath(login_dingwei.szcs_an1))
        s2.select_by_value(input_a.sucess['szcs_1'])
        s3 = Select(self.driver.find_element_by_xpath(login_dingwei.szcs_an2))
        s3.select_by_value(input_a.sucess['szcs_2'])
        s4 = Select(self.driver.find_element_by_xpath(login_dingwei.szcs_an3))
        s4.select_by_value(input_a.sucess['szcs_3'])

        # 定位我的团队
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.wddhlteam_an)).click()

        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.zxzx_ka_an2)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.zxzx_khjl_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.zxzx_dibu1_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.zxzx_dibu2_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.zxzx_dibu3_an)).click()
