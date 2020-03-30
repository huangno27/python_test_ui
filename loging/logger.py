import logging
from logging.handlers import RotatingFileHandler
from dhl_5i_web.loging import constants
class Logger:
    """
    日志输出：
    级别 - 大开关 Logger  渠道开关
    渠道 - console， file
    格式
    """
    def __init__(self, name):
        self.log = logging.getLogger(name)
        self.log.setLevel('DEBUG')

        # 设置格式
        fmt = "%(asctime)s-%(levelname)s-%(message)s [%(levelno)s:%(filename)s]"
        formatter = logging.Formatter(fmt=fmt)

        # 输出渠道
        # 1.console
        console_hander = logging.StreamHandler()
        console_hander.setLevel('DEBUG')
        console_hander.setFormatter(fmt=formatter)
        # 2.file
        # backupCount 备份个数  maxBytes 文件大小
        file_handler = RotatingFileHandler(constants.logs_file, maxBytes=1024*1024,
                                           backupCount=3, encoding='utf-8')
        file_handler.setLevel('INFO')
        file_handler.setFormatter(fmt=formatter)

        # handler添加到日志实例中
        self.log.addHandler(console_hander)
        self.log.addHandler(file_handler)

    def debug(self, msg):
        self.log.debug(msg)

    def info(self, msg):
        self.log.info(msg)

    def warning(self, msg):
        self.log.warning(msg)

    def error(self, msg):
        self.log.error(msg)

log = Logger("zhang_Test")
