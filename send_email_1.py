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
    filename = name_file+'_vulnerability.xls'

    msg = EmailMessage()
    msg['Subject'] = 'Vulnerabilidades críticas solicitada por'+' '+name_file+' '+'--Contém anexo'
    msg['From'] = 'valimfabiano@gmail.com'
    msg['To'] = (email_dest)
    password = 'cpzocyejvwzwgagv'
    msg.set_payload(corpo_email)
    msg.attach(MIMEText(text))
    """Attach a file identified by filename, to an email message"""
    with open(filename, 'rb') as fp:
        file_data = fp.read()
        maintype, _, subtype = (mimetypes.guess_type(filename)[0] or 'application/octet-stream').partition("/tmp/")
        msg.attach(file_data, maintype=maintype, subtype=subtype, filename=filename)
    # Set text content
    msg.set_content('Please see attached file')
    # Attach files
    attach_file_to_email(msg, name_file+'_vulnerability.xls')

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.send_message(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    s.quit()
