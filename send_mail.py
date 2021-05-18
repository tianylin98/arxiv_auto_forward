#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 

mail_host="smtp.office365.com"
mail_user=os.getenv("USERNAME")
mail_pass=os.getenv("PASSWORD")
port = 587
 

sender = mail_user
receivers = os.getenv("RECEIVERS").split(' ')
 
mail_msg = open('./arxiv.html', 'r').read()
message = MIMEText(mail_msg, 'html', 'utf-8')
 
subject = f'arxiv auto-forward {os.getenv("DATE")}'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP(mail_host, port)  
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(mail_user, mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
except smtplib.SMTPException as e:
    print(e)
