#!/usr/bin/env python3
import os
import smtplib
import mimetypes
import pandas as pd
from email.message import EmailMessage
from email.mime.text import MIMEText
# Create message and set text content
from email import encoders
from datetime import datetime

def send(email_dest, name_file):
    bufferSize = 64 *1024
    reader = pd.read_excel('/tmp/'+name_file+'_vulnerability.xls')
    body = reader.to_html()
    corpo_email = body
    fileAttach = ('/tmp/'+name_file+'_vulnerability.xls')

    msg = MIMEMultipart()
    msg['Subject'] = 'Vulnerabilidades críticas solicitada por'+' '+name_file+' '+'--Contém anexo'
    msg['From'] = 'valimfabiano@gmail.com'
    msg['To'] = (email_dest)
    password = 'cpzocyejvwzwgagv'
    msg.set_payload(corpo_email)
    msg.attach(MIMEText(mail_content, 'plain'))
    attach_file = open(fileAttach, 'rb')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)
    # Set text content
    msg.set_content('Please see attached file')
    payload.add_header('Content-Decomposition', 'attachment', 'filename=fileAttach')
    message.attach(payload)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    text = message.as_string()
    s.send_message(msg['From'], msg['To'], text)
    #msg.as_string().encode('utf-8'))
    s.quit()
