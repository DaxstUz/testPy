#!/usr/bin/python
# -*- coding: utf-8 -*- 
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
 
my_sender='sunyz@ieyecloud.com'    # 发件人邮箱账号
my_pass ='nbsBdxa45xNShW6c'              # 发件人邮箱密码
# my_user='2416738717@qq.com'      # 收件人邮箱账号

def mail():
    ret=True
    
    try:
        msg=MIMEText('测试患者资料完善邮件发送','plain','utf-8')
        msg['From']=formataddr(["孙有志",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["chaiyuxiao","chaiyuxiao@ieyecloud.com"])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="uz发送邮件测试"                # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,["chaiyuxiao@ieyecloud.com"],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception,e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print e
        ret=False
    return ret
 
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")