import imaplib
from my_parser import Parser


IMAP_HOST = 'mailstore.iitd.ac.in'  # imap.mail.yahoo.com
PORT = 993
USERNAME='xyz'
PASSWORD='xyz'


server = imaplib.IMAP4_SSL(IMAP_HOST, PORT)
server.login(USERNAME,PASSWORD)
status,message = server.select('INBOX')

response,msg = server.fetch(message[0],'(RFC822)')

p = Parser(msg)
p.dump_in_file()
#p.parse_msg()
p.verify_dkim(msg)


