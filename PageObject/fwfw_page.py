import time
from op_datas.fwfw_input_data import Fw_da as login_da
from yusuan_datas.fwfw_datas import Objectpage_datas_Fwfw as login_dingwei
from selenium.webdriver.common.action_chains import ActionChains
from url_datas import global_datas
from selenium.webdriver.support.wait import WebDriverWait

class Ob_fwff:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get(global_datas.base_url)
        self.driver.maximize_window()

    def ffwf_func(self,user,passwd,yzm,gj,yb):
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.index_loc)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.dl_anniu)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.user_loc)).send_keys(login_da.sucess['user'])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.password_loc)).send_keys(login_da.sucess['passwd'])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.yzm_loc)).send_keys(login_da.sucess['yzm'])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.login_button_loc)).click()
        time.sleep(1)
        an = self.driver.find_element_by_xpath(login_dingwei.wyjj_loc)
        ActionChains(self.driver).move_to_element(an).perform()
        time.sleep(1)
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.fwfw_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.gjdq_an)).send_keys(login_da.sucess['gj'])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.shuruzhi_an)).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.yb_an)).send_keys(login_da.sucess['yb'])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.shuruyoubian_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.cx_an1)).click()

        # 输入邮编自动带出城市
        # self.driver.find_element_by_xpath(login_dingwei.city_an).send_keys(login_da.sucess['city'])

        # 查询按钮暂时没做好
        # self.driver.find_element_by_xpath(login_dingwei.cx_an)

