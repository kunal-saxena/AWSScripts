#!/usr/bin/python

import smtplib

sender = 'kunal@damour.in'
receivers = ['ksaxena@gmail.com']
toadd = "Kunal <kunal_sax@yahoo.com>"
subject = "SMTP e-mail test test final - 1" 
tomessage = "Dear Kunal, " 

message = """From: Damour Services Pvt Lmt <contact@damour.in>
To:"""  + toadd + """
Subject: """ + subject + """ 

""" + tomessage + """

We are glad to see you here. 
Together we can achieve greater heights

--with regards
sales team
Damour Services Pvt Lmt

"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"

