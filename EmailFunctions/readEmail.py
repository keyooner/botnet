from imap_tools import MailBox
import const
import re
from time import sleep

def readMail(username, password):

    # Use your IMAP server for Mail
    imap_server = const.IMAP_SERVER
    with MailBox(imap_server, port=993).login(username, password, "INBOX") as mailbox:
        for msg in mailbox.fetch(criteria="ALL"):
            if msg.uid == 2 or msg.from_ == "info@twitter.com":
                print(f"===== MESSAGE ID: {msg.uid} =====")
                print(f"From: {msg.from_}")
                print(f"To: {msg.to}")
                print(f'Bcc: {msg.bcc}')
                print(f"Date: {msg.date}")
                print(f'Subject: {msg.subject}')
                print(f"Body: \n{msg.text}")

                if match := re.search(r'\d+', msg.subject):
                    print("Código recibido... es:\n")
                    print(match.group())
                    return match.group()