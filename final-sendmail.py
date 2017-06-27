#!/usr/bin/python

import smtplib



def sender():
   sender = 'contact@damour.in'
   receivers = ['ksaxena@gmail.com']
   toadd = "Kunal <ksaxena@gmail.coom>"
   subject = "Use this final template"
   tomessage = "Dear Kunal, "

   message = """From: Damour Services Pvt Lmt <contact@damour.in>
   To:"""  + toadd + """
   Subject: """ + subject + """ 

   """ + tomessage + """
   
   We are glad to see you here. 
   Together we can achieve greater heights

   --with regards
   Support team
   Damour Services Pvt Lmt

   """

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"


   

sender()