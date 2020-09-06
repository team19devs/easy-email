import smtplib, sys
from email.message import EmailMessage
from pathlib import Path
from string import Template
from time import sleep

#if __name__=="__main":
list_names = sys.argv[1:]

def auto_send(sent_name):
    for mail_account in sent_name:
        html = Template(Path("index.html").read_text())
        email = EmailMessage()
        email['from'] = "Yuldashboyev Farrux"
        email["to"] = mail_account
        email["subject"] = "Farrux sizga minnatdorchilik bildirdi!"
        print(email)
        email.set_content(html.substitute(emadress=email['to']), 'html')

        with smtplib.SMTP(host = "smtp.gmail.com", port=587) as sm:
            sm.ehlo()
            sm.starttls()
            sm.login("team19devs1901@gmail.com", 'iamdummy1')
            value = sm.send_message(email)
            if value:
                print(f"Email successfully sent to {mail_account}")
                return value
auto_send(list_names)
