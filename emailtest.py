#!/usr/bin/python3
# -*-coding:utf-8 -*-


import time
import smtplib
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 需要输入的发件人的信息
mail_Tolist=["tujiachen@gmail.com"]

mail_name=str(input("Please input your accout:"))
mail_password=str(input("Please input your email password:"))

mail_subject=str(input("Please input mail's subject:"))
mail_context=str(input("Please input mail's context:"))


def send_mail():
    msg=MIMEMultipart()
    msg['From']=mail_name
    msg['To']=";".join(mail_Tolist)
    msg['Subject']=mail_subject
    
    txt=MIMEText(mail_context)
    msg.attach(txt)
    
    smtp=smtplib.SMTP_SSL()
    smtp.connect('smtp.gmail.com:465')
    smtp.login(mail_name,mail_password)
    
    smtp.sendmail(mail_name,mail_Tolist,msg.as_string())
    
    smtp.quit()
    print("Sended sueessccful")
    
if __name__=="__main__":
    send_mail()