import smtplib, sys, os
from email.message import EmailMessage
from pathlib import Path
from string import Template
from time import sleep

list_names = sys.argv[1:]
user_message = input("OK. Send me message to send: ")
print(user_message)
def auto_send(sent_name):
    for mail_account in sent_name:
        html = Template(user_message)
        email = EmailMessage()
        email['from'] = "AnonymCybercik & team19devs"
        email["to"] = mail_account
        email["subject"] = "Join us on GitHub!"
        print(email)
        email.set_content(html.substitute(emadress=email['to']), 'html')

        with smtplib.SMTP(host = "smtp.gmail.com", port=587) as sm:
            sm.ehlo()
            sm.starttls()
            sm.login("team19devs1901@gmail.com", 'iamdummy1')
            value = sm.send_message(email)
            if email:
                print(f"Email successfully sent to {mail_account}")
                #sys.exit()
                return value


auto_send(list_names)
