import threading
import json
import requests
import smtplib
from email.mime.text import MIMEText
import time
import pymysql

# 连接测试数据库
connect = pymysql.Connect(
    host='192.168.15.104',
    port=3306,
    user='crm_rtmap',
    passwd='rtmap-911',
    db='test',
    charset='utf8'
)


def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec


def time_check():
    second = sleeptime(0, 5, 0)
    while 1 == 1:
        monitor_interface()
        time.sleep(second)


def time_clear():
    second = sleeptime(24, 0, 0)
    while 1 == 1:
        time.sleep(second)
        clear_data()



def clear_data():
    # 获取游标  每天定时执行，清理三天之前的数据
    cursor = connect.cursor()
    sqlc = "delete FROM operation_record where DATE_SUB(CURDATE(), INTERVAL 3 DAY) >= date(intime)"
    cursor.execute(sqlc)
    print("数据库每天清理执行完成", (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    connect.commit()


def monitor_interface():
    headers = {'Content-Type': 'application/json'}
    failcontent = ""
    url = ""
    # 获取游标 五分钟执行一次，遇到访问错误，发送邮件，记录入库
    cursor = connect.cursor()
    market_code = {"zhihuitu": "第一个数据库", "fslctyc": "第二个数据库", "tjdjc": "第三个数据库", "wdjt": "第四个数据库"}
    for key in market_code.keys():
        if key == 'zhihuitu':
            url = 'https://crm-api.rtmap.com/crmapi/access/auth/getcompany'
        elif key == 'fslctyc':
            url = 'https://crm-api.rtmap.com/saas2/crmapi/access/auth/getcompany'
        elif key == 'tjdjc':
            url = 'https://crm-api-t.rtmap.com/crmapi/access/auth/getcompany'
        elif key == 'wdjt':
            url = 'https://crm-api-t.rtmap.com/crmapi/access/auth/getcompany'
        data = {"customer_code": key, "user_code": "admin", "router_path": "/login"}
        dataJson = json.dumps(data)  # 将 dict转成str
        requests.packages.urllib3.disable_warnings()
        return_st = requests.post(url, data=dataJson, headers=headers, verify=False)
        # print(url, data, return_st.status_code)
        rj = return_st.json()
        # print(rj)

        if "msg" in rj and rj['msg'] == "请求错误":
            print(url, data, rj)
            failcontent = failcontent + market_code[key] + "\n"
            continue

    if len(failcontent) > 0:
        # 失败入库信息
        print("failcontent", failcontent, len(failcontent))
        sql1 = "insert INTO operation_record (indata,personnel,intime,instatus) VALUES (%s,'自动化监控',NOW(),1)"
        print(sql1)
        cursor.execute(sql1, failcontent)
        connect.commit()
        print("出现问题的数据库：", failcontent, (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    else:
        # 成功入库信息
        sql = "insert INTO operation_record (indata,personnel,intime,instatus) VALUES ('数据库访问成功','自动化监控',NOW(),0)"
        cursor.execute(sql)
        connect.commit()
        print("数据库访问成功,访问时间", (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    cursor.close()

    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # SMTP服务器
    mail_user = "tachangshuang@163.com"  # 用户名
    mail_pass = "GGVZJDVNAAHDEIOZ"  # 授权密码，非登录密码
    sender = "tachangshuang@163.com"  # 发件人邮箱(最好写全, 不然会失败)
    receivers = ["tachangshuang@rtmap.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    title = '监控SAAS CRM系统' + (time.strftime('%Y%m%d%H%M', time.localtime(time.time())))
    if len(failcontent) > 1:
        content = failcontent + "访问失败，连接不通，请紧急处理！！！"
        message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
        message['From'] = "{}".format(sender)
        message['To'] = ",".join(receivers)
        message['Subject'] = title
        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(mail_user, mail_pass)  # 登录验证
            smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
            print("mail has been send successfully.")
        except smtplib.SMTPException as e:
            print(e)


t1 = threading.Thread(target=time_check)  # 定义线程t1，线程任务为调用time_check函数，task1函数无参数
t2 = threading.Thread(target=time_clear)  # 定义线程t2，线程任务为调用time_clear函数，task2函数无参数
t1.start()  # 开始运行t1线程
t2.start()  # 开始运行t2线程
