# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 09:02:57 2023

@author: User
"""

import smtplib
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('tctourism2022@gmail.com','mvnaddmzlwkeemsi')
from_addr = 'tctourism2022@gmail.com'
to_addr = 'andycy.tw@gmail.com'
msg = 'Subject:title\nHello\nWorld!'
status = smtp.sendmail(from_addr, to_addr, msg)
if status == {}:
    print('郵件傳送成功！')
else:
    print('郵件傳送失敗...')
smtp.quit()