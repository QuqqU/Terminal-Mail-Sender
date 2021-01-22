import os
from server import Server
from config import SMTP_SERVER, SENDER, USER_ID
from email.message import EmailMessage
import getpass
from email_parser import Email_parser as ep

def get_receivers():
    recievers = []
    WORK_DIR = os.getcwd()
    with open(WORK_DIR + "/mail_sender/recievers.txt", "r") as f:
        for line in f.readlines():
            recievers.append(line.strip())
    return recievers

def main():

    try:
        PASSWORD = "wjdrldnd4037139*"#getpass.getpass("password: ")
        server = Server(SMTP_SERVER, USER_ID, PASSWORD)
        server.connect()

        print("1")

        URL = os.getcwd() + "/mail_sender/mail.txt"
        print("1")
        mail = ep(URL)     
        print("1")
        mail = mail.mail
        # mail['subject'] = "title : hello world"
        # mail['from'] = SENDER
        mail['bcc'] = get_receivers()
        # mail['cc'] =
        # mail['bcc'] = ["rldnd913@naver.com", "rldnd913@u.sogang.ac.kr"]
        # server.send(recievers, mail)
        print(mail)
        print("1")
    except Exception as e:
        print(e)
        pass


if __name__ == "__main__":
    main()
