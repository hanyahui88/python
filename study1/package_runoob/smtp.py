# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formataddr


def sendMail():
    mail_host = "smtp.exmail.qq.com"
    mail_user = "hanyahui@quandashi.com"
    mail_pass = "123qweASD"
    sender = 'hanyahui@quandashi.com'
    receivers = ['hanyahui88@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def sendHTMLMail():
    mail_host = "smtp.exmail.qq.com"
    mail_user = "hanyahui@quandashi.com"
    mail_pass = "123qweASD"
    sender = 'hanyahui@quandashi.com'
    receivers = ['hanyahui88@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    html = """<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>"""
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(html, 'html', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def sendAttachFile():
    mail_host = "smtp.exmail.qq.com"
    mail_user = "hanyahui@quandashi.com"
    mail_pass = "123qweASD"
    sender = 'hanyahui@quandashi.com'
    receivers = ['hanyahui88@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEMultipart()
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('e:\\test.txt', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    message.attach(att1)

    # 构造附件2，传送当前目录下的 runoob.txt 文件
    att2 = MIMEText(open('e:\\2016081813.jpg', 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="2016081813.jpg"'
    message.attach(att2)
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def sendHTMLImage():
    mail_host = "smtp.exmail.qq.com"
    mail_user = "hanyahui@quandashi.com"
    mail_pass = "123qweASD"
    sender = 'hanyahui@quandashi.com'
    receivers = ['hanyahui88@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    msgRoot = MIMEMultipart('related')
    msgRoot['From'] = Header("菜鸟教程", 'utf-8')
    msgRoot['To'] = Header("测试", 'utf-8')
    subject = 'Python SMTP 邮件测试'
    msgRoot['Subject'] = Header(subject, 'utf-8')

    msgHTML = MIMEMultipart('alternative')
    msgRoot.attach(msgHTML)

    mail_msg = """
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
    <p>图片演示：</p>
    <p><img src="cid:image1"></p>
    """
    msgHTML.attach(MIMEText(mail_msg, 'html', 'utf-8'))

    fp = open('e:\\2016081813.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, msgRoot.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def mail():
    mail_host = "smtp.exmail.qq.com"
    my_sender = 'hanyahui@quandashi.com'  # 发件人邮箱账号
    my_pass = '123qweASD'  # 发件人邮箱密码
    my_user = 'hanyahui88@163.com'  # 收件人邮箱账号，我这边发送给自己
    ret = True
    try:
        msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL(mail_host, 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


sendHTMLImage()
