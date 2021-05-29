import smtplib
from email.mime.text import MIMEText

PORT=25
SMTP_SERVER='smtp.iitd.ac.in'
USERNAME='xyz'
PASSWORD='xyz'

server= smtplib.SMTP(SMTP_SERVER,PORT)
server.ehlo()
server.starttls()
server.ehlo()
server.login(USERNAME,PASSWORD)

body="The OTP for transferring Rs 1,00,000 to your friend's account is 256345"
msg = MIMEText(body,'plain','utf-8')
msg['From'] = USERNAME
msg['To'] = USERNAME
msg['Subject'] = 'Dummy mail for OTP transfer'
server.sendmail(USERNAME,USERNAME,msg.as_string())
