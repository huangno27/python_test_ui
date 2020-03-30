import time
from op_datas.cwfw_input_datas import Wycs_da as input_a
from yusuan_datas.cwfw_data import Objectpage_datas_Cxhfw as login_dingwei
from selenium.webdriver.common.action_chains import ActionChains
from url_datas import global_datas
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Ob_cxfw_two:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get(global_datas.base_url)
        self.driver.maximize_window()

    # 快件查询
    def cxhfw_func(self,user,passwd,yzm,dh):
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
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.cwfw_an)).click()

        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.cwfw_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.wdzh_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.zxfk_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.ydh_an))#.send_keys(input_a.sucess['dh'])     # 现阶段有默认值
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.PIN_CODE_an))#.send_keys(input_a.sucess['PINCODE'])
        # 无支付码 -> 赊销业务款项 其他2个没写呢
        # 传一个账号 清除 再点选择按钮
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.DHL_sxzh_an)).send_keys("123456789")
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.DHL_sxzh_an)).clear()
        # 点击赊销账号的选择
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.DHL_SX_1_an)).click()
        # 添加DHL赊销账号
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.tj_sxzh_input_an)).send_keys("huang")
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.tj_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.xz_an)).click()

        # 勾选
        # WebDriverWait(driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.tj_xzk_an)).click()
        # WebDriverWait(driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.tj_cygs_an)).click()
        # 取消选择
        # WebDriverWait(driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.tj_xzk_an)).click()
        # WebDriverWait(driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.tj_cygs_an)).click()
        # 删除暂时先不点
        # WebDriverWait(driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.sc_an)).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.qx_an)).click()

        # 费用类型、付款金额 DHL账单号、DHL税务发票号、备注
        s1 = Select(self.driver.find_element_by_xpath(login_dingwei.fylx_an))
        s1.select_by_value(input_a.sucess['fylx'])

        WebDriverWait(self.driver, 10, 0.5).until(lambda diver:self. driver.find_element_by_xpath(login_dingwei.fkje_an)).send_keys("100")
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver:self. driver.find_element_by_xpath(login_dingwei.dhl_zdh_an)).send_keys("6010203040")
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.dhl_swfph_an)).send_keys("6070809010")
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver:self. driver.find_element_by_xpath(login_dingwei.bz_an)).send_keys("测试脚本留言!")
        # 添加新订单/取消新订单
        time.sleep(3)
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.tj_newdd_an)).click()
        time.sleep(3)
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.qx_newdd_an)).click()

        # 提交订单并支付
        # WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.tjiaoddzf_an)).click()
        # WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.zxfk_an)).click()
        # WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.zxfk_an)).click()

        # 点击支付
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.zf_an)).click()
        # WebDriverWait(self.driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.yx_an)).send_keys(input_a.sucess['yx'])
        # WebDriverWait(self.driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.sjh_an)).send_keys(input_a.sucess['sjh'])
        # WebDriverWait(self.driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.kqzf_an)).click() # 快钱支付
        # WebDriverWait(self.driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.smzf_an)).click() # 扫码支付
        # WebDriverWait(self.driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.ljzf_an)).click() # 立即支付
        # WebDriverWait(self.driver, 10, 0.5).until(lambda diver: driver.find_element_by_xpath(login_dingwei.kjcx_an)).click() # 快件查询
        WebDriverWait(self.driver, 10, 0.5).until(lambda diver: self.driver.find_element_by_xpath(login_dingwei.qx2_an)).click()  # 取消
