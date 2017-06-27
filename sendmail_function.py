#!/usr/bin/python
import sys

def sendmail(FromM,ToM,ToName,ToSubject,BodyM):
   import smtplib

   sender = FromM
   receivers = ToM
   toadd = 'customer@damour.in'
   subject = ToSubject
   tomessage = "Dear " + ToName 
   
   message = """From: Damour Services Pvt Lmt <contact@damour.in>
To:"""  + toadd + """
Subject:""" + subject + """ 

""" + tomessage + """
   """ + BodyM + """ 
   """ 


   try:
      smtpObj = smtplib.SMTP('localhost')
      smtpObj.sendmail(sender, receivers, message)
      print "Successfully sent email"
   except SMTPException:
      print "Error: unable to send email"

def readinput(valpassed):
   import re
   
   pattern1 = re.compile(r"FromMessage", re.I) 
   pattern2 = re.compile(r"ToMessage", re.I) 
   pattern3 = re.compile(r"BodyMessage", re.I)
   pattern4 = re.compile(r"ToName", re.I)
   pattern5 = re.compile(r"ToSubject",re.I)
   count = 1
   FromMessage=""
   ToMessage=""
   BodyMessage=""
   with open('mail','r') as fr:   
      for line in fr:
         #fr.__next__()
         if valpassed == "FromMessage":
            if pattern1.search(line) != None:
               fromadd=line.split(':',1)
               return fromadd[1]

         if valpassed == "ToMessage":
            if pattern2.search(line) != None:
               toadd=line.split(':',1)
               return toadd[1]

         if valpassed == "ToName":
            if pattern4.search(line) != None:
               toadd=line.split(':',1)
               return toadd[1]

         if valpassed == "ToSubject":
            if pattern5.search(line) != None:
               toadd=line.split(':',1)
               return toadd[1]

         if valpassed == "BodyMessage":
            if pattern3.search(line) != None or count > 1:
               if count > 1: BodyMessage = BodyMessage + line 
               count=count+1

   return BodyMessage 
      
def main():
   #filename=sys.argv[1]
   
   FromMessage=readinput("FromMessage")
   ToMessage=readinput("ToMessage")
   ToName=readinput("ToName")
   ToSubject=readinput("ToSubject")
   BodyMessage=readinput("BodyMessage")

   sendmail(FromMessage,ToMessage,ToName,ToSubject,BodyMessage)
	

if __name__=="__main__":
   main()

