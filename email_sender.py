import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path("index.html").read_text())
email = EmailMessage()
email['from'] = "Yuldashboyev Farrux"
email["to"] = 'team19devs@gmail.com'
email["subject"] = "Farrux challenged you on SoloLearn"
print(email)
email.set_content(html.substitute(emadress=email['to']), 'html')

with smtplib.SMTP(host = "smtp.gmail.com", port=587) as sm:
    sm.ehlo()
    sm.starttls()
    sm.login("team19devs1901@gmail.com", 'iamdummy1')
    sm.send_message(email)
