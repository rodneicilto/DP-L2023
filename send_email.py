import os
import smtplib
import pandas as pd
import email.message
from email import encoders
from datetime import datetime
from email.mime.applications import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def send(email_dest,name_file):
    bufferSize = 64 * 1024
    reader = pd.read_excel('/tmp/'+name_file+'_vulnerability.xls')
    body = reader.to_html()
    corpo_email = body

    msg = email.message.Message()
    msg['Subject'] = "Vulnerabilidades Críticas Data"+name_file
    msg['From'] = 'valimfabiano@gmail.com'
    msg['To'] = (email_dest)
    password = 'cpzocyejvwzwgagv'
    #msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    msg.attach(MIMEText(body, 'plain'))
    filename = name_file+'_vulnerability.xls'
    attachment = open("/tmp/")

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename = %s" % filename)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    #print('Email enviado')
#s.quit()
