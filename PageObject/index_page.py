import time
from yusuan_datas.Op_datas import Objectpage_datas as dw
from selenium.webdriver.remote.webdriver import WebDriver



class Indexpage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def check_user_ele_exists(self):
        # 先等待首页元素出现
        time.sleep(5)
        self.driver.find_element_by_xpath(*dw.index_loc)
        # 判断元素是否存在 get_element 能找到即存在
        try:
            self.driver.find_element(*dw.login_err_loc)
        except:
            return False
        else:
            return True

#