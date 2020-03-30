import time
from op_datas.dlfw_input_data import Wycs_da as input_a
from yusuan_datas.dlfw_datas import Objectpage_datas_Dlfw as login_dingwei
from selenium.webdriver.common.action_chains import ActionChains
from url_datas import global_datas
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class Ob_cxfw_dlpt:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get(global_datas.base_url)
        self.driver.maximize_window()

    # 代理平台
    def dlpt_func(self,user,passwd,yzm,dh1,dh2,dh3,lx1,lx2,lx3,dh4,lx4,lx5,lx6,gj,city):
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.index_loc)).click()
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.dl_anniu)).click()
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.user_loc)).send_keys(input_a.sucess['user'])
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.password_loc)).send_keys(input_a.sucess['passwd'])
        WebDriverWait(self.driver,10,0.5).until(lambda diver:self.driver.find_element_by_xpath(login_dingwei.yzm_loc)).send_keys(input_a.sucess['yzm'])
        self.driver.find_element_by_xpath(login_dingwei.login_button_loc).click()
        # 鼠标悬浮选择
        time.sleep(3)
        an = self.driver.find_element_by_xpath(login_dingwei.dlpt_an)
        ActionChains(self.driver).move_to_element(an).perform()
        # 点击新的查询
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.syxdcx_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.wdzh_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.xdcx_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.zxkscx_an)).send_keys(input_a.sucess["dh1"])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.scan_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.zxkscx_an)).send_keys(input_a.sucess["dh2"])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.cxan_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.qtcxxq_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.fhxdcx_an)).click()

        # 定位我的查询 ->DHL客户端发起的查询
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.wdcx_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.dhlkfd_ydh_an)).send_keys(input_a.sucess["dh3"])
        s1 = Select(self.driver.find_element_by_xpath(login_dingwei.zh_an))
        s1.select_by_index(input_a.sucess['lx1'])
        s2 = Select(self.driver.find_element_by_xpath(login_dingwei.zt_an))
        s2.select_by_index(input_a.sucess['lx2'])
        s3 = Select(self.driver.find_element_by_xpath(login_dingwei.cxlb_an))
        s3.select_by_index(input_a.sucess['lx3'])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.cx_an)).click()
        time.sleep(2)

        # 定位我的查询 ->我发起的查询
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.wfqdcx_an)).click()
        time.sleep(2)
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.wfqdcx_ydh_an)).send_keys(input_a.sucess["dh4"])
        s4 = Select(self.driver.find_element_by_xpath(login_dingwei.wfqdcx_zh_an))
        s4.select_by_index(input_a.sucess['lx4'])
        s5 = Select(self.driver.find_element_by_xpath(login_dingwei.wfqdcx_zt_an))
        s5.select_by_index(input_a.sucess['lx5'])
        s6 = Select(self.driver.find_element_by_xpath(login_dingwei.wfqdcx_lb_an))
        s6.select_by_index(input_a.sucess['lx6'])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.wfqdcx_cx_an)).click()

        # 定位我的查询 ->已关闭的查询
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.ygbcx_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.ygbydh_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.ygbzh_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.ygbcxan_an)).click()

        # 定位查询数据统计
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.cxsjtj_an)).click()

        # 定位三字代码查询
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.szdmcx_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.gjdq_an)).send_keys(input_a.sucess["gj"])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.dj_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.city_an)).send_keys(input_a.sucess["city"])
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.city_xz_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.szdmcx_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.szdmcxan_an)).click()

        # 定位代理知识库 有问题 代码定位时 有悬浮遮挡
        # WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.dlzsk_an)).click()
