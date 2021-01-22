import smtplib
from email.message import EmailMessage

class Server:

    def __init__(self, SMTP_SERVER, USER_ID, PASSWORD):
        self.server = smtplib.SMTP(SMTP_SERVER)
        self.user_id = USER_ID
        self.password = PASSWORD
 
    def connect(self):
        self.server.starttls()
        self.server.login(self.user_id, self.password)
        
    def send(self, mail: EmailMessage):
        mail.set_charset("utf-8")
        self.server.send_message(mail)

    def disconnect(self):
        self.server.quit()
        



    