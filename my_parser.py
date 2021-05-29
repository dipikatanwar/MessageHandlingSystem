import smtplib
from email.mime.text import MIMEText
import imaplib
import email
from email.header import decode_header
from base64 import b64encode, b64decode
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import dkim


class Parser():
    def __init__(self,msg):
        self.msg = msg

    def get_DKIM_params(self,dkim_header):
        param = dkim_header.split(';')
        ans = { p.split('=')[0].strip() : p.split('=')[1].strip()  for p in param}
        return ans

    def verify_dkim(self, body):
        for m in self.msg:
            if type(m) == tuple:
                i = email.message_from_bytes(m[1])
                params ={} 
                params = self.get_DKIM_params(i['DKIM-Signature'])
                print("Below are parsed DKIM parameters : ")
                print(params)
                print("-------------------------------------")
                selector = params['s']
                if dkim.verify(m[1]):
                    print('DKIM verification successful')
                else:
                    print('DKIM verification failed')    

    def showMessage(self,msg):
        print("Printing general mail fields\n")
        email_from = msg['From']
        email_to = msg['To']
        subject = msg['Subject']
        print('From : ')
        print(email_from)
        print('To : ')
        print(email_to)
        print('Subject : ')
        print(subject)
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                print('Body : ')
                print(body)
                print("\n")
            else:
                continue

    def security_params(self,msg):
        received = msg['Received']
        print(received)
        Auth_results = msg['Authentication-Results']
        print(Auth_results)
        DMARC_Filter = msg['DMARC-Filter']
        print(DMARC_Filter)

    def parse_msg(self):
        for m in self.msg:
            if type(m) == tuple:
                i = email.message_from_bytes(m[1])
                self.showMessage(i)
                self.security_params(i)

    def dump_in_file(self):
        fp = open('out.txt', "w")
        for m in self.msg:
            if type(m) == tuple:
                i = email.message_from_bytes(m[1])
                i=i.as_string()
                fp.write(i)       

