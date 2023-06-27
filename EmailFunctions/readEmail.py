from imap_tools import MailBox
import const
import re
import datetime
from time import sleep

# Get account details
def readMail(username, password):

    # Use your IMAP server for Mail
    imap_server = "mail.raptoragency.es"

    with MailBox(imap_server, port=993).login(username, password, "INBOX") as mailbox:
        for msg in mailbox.fetch(criteria="ALL"):
            print(f"===== MESSAGE ID: {msg.uid} =====")
            print(f"From: {msg.from_}")
            print(f"To: {msg.to}")
            print(f'Bcc: {msg.bcc}')
            print(f"Date: {msg.date}")
            print(f'Subject: {msg.subject}')
            print(f"Body: \n{msg.text}")

def readMailTwitter(username, password):
    # Use your IMAP server for Mail
    imap_server = "mail.raptoragency.es"
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


def readMailSuspiciousActivity(username, password):
    # Use your IMAP server for Mail
    imap_server = const.IMAP_SERVER
    with MailBox(imap_server, port=993).login(username, password, "INBOX") as mailbox:
        messages = list(mailbox.fetch(criteria="ALL"))
        for msg in reversed(messages):
            if ("Your Twitter confirmation code is" in msg.subject
                and (datetime.datetime.now(datetime.timezone.utc) - msg.date).total_seconds() <= 60):
                print(f"===== MESSAGE ID: {msg.uid} =====")
                print(f"From: {msg.from_}")
                print(f"To: {msg.to}")
                print(f'Bcc: {msg.bcc}')
                print(f"Date: {msg.date}")
                print(f'Subject: {msg.subject}')
                print(f"Body: \n{msg.text}")

                if code_match := re.search(r'Your Twitter confirmation code is (\w+)', msg.subject):
                    return code_match[1]
                else:
                    return None