import os
import smtplib
import pandas as pd
import email.message
from email import encoders
from datetime import datetime

def send(email_dest):
    encoders.encode_base64(att)
    reader = pd.read_excel('Vulnerability.xls')
    body = reader.to_html()
    corpo_email = body

    msg = email.message.Message()
    msg['Subject'] = "Vulnerabilidades Críticas Data"
    msg['From'] = 'valimfabiano@gmail.com'
    msg['To'] = email_dest
    password = 'cpzocyejvwzwgagv' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'],msg['To'],msg.as_string())
    #print('Email enviado')
    s.quit()
