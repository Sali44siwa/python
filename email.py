import smtpd
import smtplib
sender="salomewaruguru254@gmail.com"
receiver="joemusya254@gmail.com"   
password="sally4416."
subject="python email test"
body="hello i managed to write this email in python."

#header
message=f'''From:{sender}
To:{receiver}
Subject:{subject}\
    {body}
'''
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
try:
    
  server.login(sender,password)
  print("logged in...")
  server.sendmail(sender,receiver,message)
  print("email was sent")
except smtplib.SMTPException as e:
    print("error",e)
    