import pandas as pd
import case.vip_info.login
import requests
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib

"""读取Excel接口路由，入参。返回执行结果、发送邮件"""

token = case.vip_info.login.test_login()


def test_readMyExcel():
    headers = {'Content-Type': 'application/json'}
    uri = "https://crm-api.rtmap.com"
    df = pd.read_excel(u"../case/vip_info/vip_info_t1.xlsx")  # 这个会直接默认读取到这个Excel的第一个表单
    data = df.loc[:, ['接口路由', '入参']].values  # 读所有行的title以及data列的值，这里需要嵌套列表
    i = 0
    j = 0
    requests.packages.urllib3.disable_warnings()
    content = 'CRM B端常规业务自动化回归测试'

    for data1 in data:
        time.sleep(1)
        j = j + 1
        url = uri + data1[0]
        dataJson = data1[1].replace('2cab5e6d0ff1b9ea82083d0109139c91', token).encode('utf-8')
        return_st = requests.post(url=url, data=dataJson, headers=headers, verify=False)
        rj = return_st.json()
        if "message" in rj and rj['message'] == "请求成功":
            i = i + 1
            content = content + '\r\n' + '{0}'.format(data1[0])
            print("@@@@@@@@@@@第", i, "个接口数据", url, dataJson, rj)
        elif "msg" in rj and rj['msg'] == "请求错误":
            content = content + "请求错误" + '{0}'.format(data1[0])
            print("@@@@@@@@接口执行失败，接口路由为", url, dataJson)
    content = content + '\r\n' + "执行成功接口有" + str(i) + "个"
    return content


# 定义发邮件
def test_send_mail(file_path):
    f = open(file_path, 'rb')
    mail_body = f.read()
    f.close()

    smtpserver = 'smtp.163.com'
    # 设置登录邮箱的账号和授权密码
    sender = 'tachangshuang@163.com'
    password = "GGVZJDVNAAHDEIOZ"
    # 可添加多个收件人的邮箱
    receives = ['tachangshuang@rtmap.com']
    # 构造邮件对象
    msg = MIMEMultipart('mixed')
    # 定义邮件的标题
    subject = 'CRM B端自动化 ' + (time.strftime('%Y%m%d%H%M', time.localtime(time.time())))
    # HTML邮件正文，定义成字典
    msg['Subject'] = Header(subject, "utf-8")
    msg['From'] = sender
    msg['To'] = ','.join(receives)
    # 构造文字内容
    text_plain = MIMEText(test_readMyExcel(), 'html', 'utf-8')
    msg.attach(text_plain)
    # 构造附件
    text_attr = MIMEText(mail_body, 'base64', 'utf-8')
    text_attr["Content-Type"] = 'application/octet-stream'
    text_attr['Content-Disposition'] = 'attachment; filename = "test.html"'
    msg.attach(text_attr)

    # 邮箱设置时勾选了SSL加密连接，进行防垃圾邮件，SSL协议端口号要使用465
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    # 向服务器标识用户身份
    smtp.helo(smtpserver)
    # 向服务器返回确认结果
    smtp.ehlo(smtpserver)
    # 登录邮箱的账号和授权密码
    smtp.login(sender, password)

    print("开始发送邮件...")
    # 开始进行邮件的发送，msg表示已定义的字典
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("已发送邮件")
