import time
from op_datas.ffwd_datas import Fwwd_da as login_da
from yusuan_datas.fwwd_datas import Objectpage_datas_fw as login_dingwei
from selenium.webdriver.common.action_chains import ActionChains
from url_datas import global_datas
from selenium.webdriver.support.select import Select

class Op_ffwd:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(global_datas.base_url)
        self.driver.maximize_window()

    def ffwd_page(self, user, passwd, yzm, cs, qx):
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
        self.driver.find_element_by_xpath(login_dingwei.fwwd_an).click()
      # driver.find_element_by_xpath(login_dingwei).click()

        s1 = Select(self.driver.find_element_by_xpath(login_dingwei.xzdq1_an))
        s1.select_by_value(login_da.sucess['cs'])
        s2 = Select(self.driver.find_element_by_xpath(login_dingwei.xzdq2_an))
        s2.select_by_value(login_da.sucess['qx'])
        time.sleep(2)

# 全部、服务网点、大学服务网点
        # driver.find_element_by_xpath(login_dingwei.qb_an).click()
        # driver.find_element_by_xpath(login_dingwei.fwwd_an1).click()
        # driver.find_element_by_xpath(login_dingwei.dxfwwd_an).click()
# 定位分享和立即发送按钮
        # driver.find_element_by_xpath(login_dingwei.share_an).click()
        # driver.find_element_by_xpath(login_dingwei.dxkdjs_an).click()
        self.driver.find_element_by_xpath(login_dingwei.tq_an).click()

