import smtplib
from email.mime.text import MIMEText
import time
import case.vip_info.ReadExcelInterface as Tri

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "tachangshuang@163.com"  # 用户名
mail_pass = "GGVZJDVNAAHDEIOZ"  # 授权密码，非登录密码
sender = "tachangshuang@163.com"  # 发件人邮箱(最好写全, 不然会失败)
receivers = ["tachangshuang@rtmap.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
title = 'CRM B端自动化 ' + (time.strftime('%Y%m%d%H%M', time.localtime(time.time())))


def sendemail():
    content = Tri.readMyExcelSendEmail()
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
