import time
from yusuan_datas.jijian_datas import Objectpage_datas_jijian as jjys
from selenium.webdriver.common.action_chains import ActionChains
from yusuan_datas.jijian_datas import Objectpage_datas_jijian as login_ys
from selenium.webdriver.support.select import Select
from op_datas import wyjj_datas as jjdata



class Woyao_jj:

    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()


    def dw_jj(self,user,passwd,yzm,dh,gj,dq,yb,jz,sl,tz,chang,kuan,gao,zl):
        # dh,gj,dq,yb,jz,sl,zl1,chang,kuan,gao,zl2
        # 运单号，国家，城市，邮编，价值，数量，重量1，长，宽，高，重量2
        time.sleep(2)
        self.driver.find_element_by_xpath(login_ys.index_loc).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(login_ys.dl_anniu).click()
        self.driver.find_element_by_xpath(login_ys.user_loc).send_keys(jjdata.sucess['user'])
        self.driver.find_element_by_xpath(login_ys.password_loc).send_keys(jjdata.sucess['passwd'])
        self.driver.find_element_by_xpath(login_ys.yzm_loc).send_keys(jjdata.sucess['yzm'])
        time.sleep(2)
        self.driver.find_element_by_xpath(login_ys.login_button_loc).click()

        time.sleep(2)
        an = self.driver.find_element_by_xpath(jjys.jj_loc)
        ActionChains(self.driver).move_to_element(an).perform()
        # 定位到预约取件
        time.sleep(1)
        self.driver.find_element_by_xpath(jjys.yy_qujian).click()
        time.sleep(2)
        # 输入单号 点查询
        self.driver.find_element_by_xpath(jjys.ydh_srk).send_keys(jjdata.sucess['ydh'])
        self.driver.find_element_by_xpath(jjys.ydh_cxan).click()

        # 定位到运费时效
        self.driver.find_element_by_xpath(jjys.yfsx_anniu).click()
        time.sleep(2)
        # 定位输入框 输入国家城市和编号 寄件和收件
        self.driver.find_element_by_xpath(jjys.contory_an).send_keys(jjdata.sucess['gj'])
        self.driver.find_element_by_xpath(jjys.fj_city_an).send_keys(jjdata.sucess['city'])
        self.driver.find_element_by_xpath(jjys.fj_address_an).send_keys(jjdata.sucess['yb'])

        # 暂时有错
        # driver.find_element_by_xpath(jjys.sj_city_an).send_keys("BEIJING")
        # driver.find_element_by_xpath(jjys.sj_address_an).send_keys("072700")

        # 定位下面的详情信息
        self.driver.find_element_by_xpath(jjys.sbjz_an).send_keys(jjdata.sucess['jz'])
        # 定位下拉框
        s1 = Select(self.driver.find_element_by_xpath(jjys.js_an))
        s1.select_by_value(jjdata.sucess['sl'])
        time.sleep(2)

        # 定位输入重量长宽高输入数据 并清空数据
        self.driver.find_element_by_xpath(jjys.kj_zl_an).send_keys(jjdata.sucess['zl1'])
        self.driver.find_element_by_xpath(jjys.kj_chang_an).send_keys(jjdata.sucess['chang'])
        self.driver.find_element_by_xpath(jjys.kj_kuan_an).send_keys(jjdata.sucess['kuan'])
        self.driver.find_element_by_xpath(jjys.kj_gao_an).send_keys(jjdata.sucess['gao'])
        self.driver.find_element_by_xpath(jjys.qk_an).click()
        time.sleep(5)
        # 切到文件栏 定位重量进行选择,下拉框选择
        self.driver.find_element_by_xpath(jjys.wj_an).click()
        s2 = Select(self.driver.find_element_by_xpath(jjys.zlxz_an))
        s2.select_by_value(jjdata.sucess['wjzl'])
        time.sleep(2)
        self.driver.find_element_by_xpath(jjys.qk_an).click()

        # 退出登录
        self.driver.find_element_by_xpath(jjys.qt_an).click()
        time.sleep(2)

