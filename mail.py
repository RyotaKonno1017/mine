#! /usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
server_IP = "127.0.0.1"  # 送信先サーバのIPアドレス(今回は"127.0.0.1")に変更する
n = 10
for i in range(n):
    From = 'foo'+(str(i+1))+'@example.com'
    To   = 'bar@example.com'
    msg = MIMEText('Hello, World!\n')
    msg['Subject'] = 'Test Subject'
    msg['From'] = From 
    msg['To'] = To
    server = smtplib.SMTP(server_IP)
    server.sendmail(From, [To], msg.as_string())
   
server.quit()