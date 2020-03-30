import time
# from op_datas.fqsp_input_datas import Fqsp_da as input_a
from op_datas import fqsp_input_datas as input_a
from yusuan_datas.fqsp_data import Objectpage_datas_Dlfw as login_dingwei
from selenium.webdriver.common.action_chains import ActionChains
from url_datas import global_datas
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Ob_cxfw_sq:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get(global_datas.base_url)
        self.driver.maximize_window()

    # 快件查询
    def cxhfw_func(self,user,passwd,yzm,dh,申请人,lxdh,dh1,kjnr,spje):
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
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.wycx_an)).click()

        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.wdzh_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.wdzh_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.kjcx_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.srdh_an)).send_keys(input_a.sucess['单号'])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.djcx_an)).click()
        time.sleep(2)
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.djkjsp_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.ty_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.sqr_an)).send_keys(input_a.sucess['申请人'])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.dhh_an)).send_keys(input_a.sucess['联系电话'])
        time.sleep(3)
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.ydh_an)).send_keys(input_a.sucess['运单号'])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.kjnr_an)).send_keys(input_a.sucess['快件内容'])
        time.sleep(1)
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.spje_an)).send_keys(input_a.sucess['索赔金额'])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.xzk_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.tj_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.tc_an)).click()
        time.sleep(3)




# driver = webdriver.Chrome()
# driver.get(global_datas.base_url)
# driver.maximize_window()
#
#
# driver.find_element_by_xpath(login_dingwei.index_loc).click()
# time.sleep(2)
# driver.find_element_by_xpath(login_dingwei.dl_anniu).click()
# driver.find_element_by_xpath(login_dingwei.user_loc).send_keys(input_a.sucess['user'])
# driver.find_element_by_xpath(login_dingwei.password_loc).send_keys(input_a.sucess['passwd'])
# driver.find_element_by_xpath(login_dingwei.yzm_loc).send_keys(input_a.sucess['yzm'])
# driver.find_element_by_xpath(login_dingwei.login_button_loc).click()
# time.sleep(3)
#
# an = driver.find_element_by_xpath(login_dingwei.cxhfw_an)
# ActionChains(driver).move_to_element(an).perform()
#
# driver.find_element_by_xpath(login_dingwei.wycx_an).click()
# driver.find_element_by_xpath(login_dingwei.wdzh_an).click()
# driver.find_element_by_xpath(login_dingwei.kjcx_an).click()
# driver.find_element_by_xpath(login_dingwei.srdh_an).send_keys("1023710730 ")   # 把txt文件里的单号替换到这里
# driver.find_element_by_xpath(login_dingwei.djcx_an).click()
# time.sleep(2)
# driver.find_element_by_xpath(login_dingwei.djkjsp_an).click()
# time.sleep(2)
# driver.find_element_by_xpath(login_dingwei.ty_an).click()
#
# driver.find_element_by_xpath(login_dingwei.sqr_an).send_keys("张三")
# driver.find_element_by_xpath(login_dingwei.dhh_an).send_keys("13800138000")
# time.sleep(1)
# driver.find_element_by_xpath(login_dingwei.ydh_an).send_keys("2362803332")
# time.sleep(1)
# driver.find_element_by_xpath(login_dingwei.kjnr_an).send_keys("快件内容")
# time.sleep(1)
# driver.find_element_by_xpath(login_dingwei.spje_an).send_keys("100")
# time.sleep(1)
# driver.find_element_by_xpath(login_dingwei.xzk_an).click()
# time.sleep(1)
# driver.find_element_by_xpath(login_dingwei.tj_an).click()
