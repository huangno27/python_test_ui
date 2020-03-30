import os
import unittest
import time
import HTMLTestRunner
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 读取当前脚本真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))


def add_case(caseName="Testcases",rule="test*.py"):
    # 用例文件夹
    case_path = os.path.join(cur_path, caseName)
    if not os.path.exists(case_path):os.mkdir(case_path)
    print("test case path: %s"%case_path)

    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    print(discover)
    return discover

def run_case(all_case, reportName = "report"):
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, reportName)
    if not os.path.exists(report_path): os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now+"_result.html")
    print("report_path:%s"%report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="DHL项目5i-UI自动化测试报告，内容如下： ",
                                           description=u'用例执行情况： ')

    runner.run(all_case)
    fp.close()

def get_report_new(report_path):
    # 获取最新测试报告
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path,fn)))
    print(u'最新的测试报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def send_mail(sender, psw, receiver, smtp_server, report_file, port):
    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset="utf-8")
    msg["Subject"] = u"DHL项目5ipc端UI自动化测试报告"
    msg["from"] = sender
    msg["to"] = psw
    msg.attach(body)

    # 添加附件
    att = MIMEText(open(report_file, "rb").read(),"base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Comtent-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtp_server, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server, port)

    # 账号密码
    smtp.login(sender,psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("测试报告邮件已发出")

if __name__ == '__main__':
    # 加载
    all_case = add_case()
    # 执行
    run_case(all_case)
    report_path = os.path.join(cur_path, "report")
    report_file = get_report_new(report_path)
    # 配置邮箱 发送邮件
    from config_data import read_config
    sender = read_config.sender
    psw = read_config.psw
    smtp_server = read_config.smtp_server
    port = read_config.port
    receiver = read_config.receiver
    send_mail(sender, psw, receiver, smtp_server, report_file, port)

