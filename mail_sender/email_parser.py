from email.message import EmailMessage


class Email_parser:

    def __init__(self, URL):
        with open(URL, "r") as f:
            self.mail = EmailMessage()
            print(2)
            self.mail['subject'] = f.readline()
            print(2)
            self.mail.set_content(f.read())

