import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import pandas as pd

def send(email_fsite, name_fsite):
    
    #Servidor de email e variaveis
    fileAttach = (name_fsite+"_vulnerability.xls")
    bufferSize = 64 * 1024
    password = "cpzocyejvwzwgagv"
    login = 'valimfabiano@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(login, password)
    reader = pd.read_excel('/tmp/'+name_fsite+'_vulnerability.xls')
    body = reader.to_html()
    corpo_email = body
    
    #Corpo do email
    email_msg = MIMEMultipart()
    email_msg['Subject'] = 'Vulnerabilidades Críticas Data '+ datetime.today().strftime("%Y-%m-%d %H:%M:%S") #pega a data atual
    email_msg['From'] = login
    email_msg['To'] = email_fsite
    email_msg.attach(MIMEText("Prezado, "+name_fsite))
    email_msg.attach(MIMEText("Segue abaixo a colsuta sobre vulnerabilidades. Em anexo, segue planilha do excel com dados completos",'Plain'))
    email_msg.attach(MIMEText(corpo_email,'html'))
    
    #Anexar arquivo
    attach_file = open('/tmp/'+name_fsite+'_vulnerability.xls', 'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attach_file.read())
    encoders.encode_base64(att)
    
    #Adiciona o cabeçalho no tipo anexo de email
    att.add_header('Content-Disposition',f'attachment; filename={fileAttach}')
    
    #fecha o arquivo
    attach_file.close()
    
    #insere no corpo do email
    email_msg.attach(att)
    
    #envia email
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())
    
    #encerra o servidor
    server.quit()
