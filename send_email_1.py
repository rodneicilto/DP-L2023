import os
import smtplib
# import LoginData
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import pandas as pd
#import pyAesCrypt



#* SMTP - Simple Mail transfer protocol
#* Para criar o servidor e enviar o email


#nome_da_planilha = "VulnerabilidadesSolicitadas"

def send(email_fsite, name_fsite):
    
    nome_da_planilha = name_fsite+'_vulnerability.xls'

    #!-------------------------------------------------------------------------------------------------------------
    #!1 - Inicia servidor
    #!-------------------------------------------------------------------------------------------------------------
    bufferSize = 64 * 1024
    password = "cpzocyejvwzwgagv"
    #host = LoginData.host
    #port = LoginData.port
    #login = LoginData.login
    #password = LoginData.password
    #os.remove("LoginData.py")
    login = 'valimfabiano@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com: 587')
    #server.ehlo()
    server.starttls()
    server.login(login, password)
    reader = pd.read_excel('/tmp/'+name_fsite+'_vulnerability.xls')
    body = reader.to_html()
    corpo_email = body



    #!-------------------------------------------------------------------------------------------------------------
    #!2 - Constroi o email tipo MIME -- texto
    #!-------------------------------------------------------------------------------------------------------------

    #todo aqui embaixo, neste grupo, eu verifico quais itens da severidade possuem valor menor q 7 e excluo suas linhas do q ira no corpo do email
    email_msg = MIMEMultipart()
    email_msg['Subject'] = 'Vulnerabilidades Críticas Data '+ datetime.today().strftime("%Y-%m-%d %H:%M:%S") #pega a data atual
    email_msg['From'] = login
    email_msg['To'] = email_fsite
    email_msg.attach(MIMEText("Prezado, "+name_fsite))
    email_msg.attach(MIMEText("Segue abaixo a colsuta sobre vulnerabilidades. Em anexo, segue planilha do excel com dados completos",'Plain'))
    email_msg.attach(MIMEText(corpo_email,'html'))

    # print("----------------------------------------")
    # print("----------------------------------------")
    # print(corpo_email)
    # print("----------------------------------------")
    # print("----------------------------------------")

    #!-------------------------------------------------------------------------------------------------------------
    #!3 - Inserção de anexo
    #!-------------------------------------------------------------------------------------------------------------

    #Abre o arquivo em modo leitura e binary
    # path_file_attach = os.path.dirname(os.path.realpath(__file__)) + "\\" + nome_da_planilha + ".xlsx"
    # attchment = open(path_file_attach, 'rb')
    attach_file = open('/tmp/'+name_fsite+'_vulnerability.xls', 'rb')

    #Lê o arquivo em modo binário e coloca ele no email codificado em base 64 (que é o que o email precisa)
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attach_file.read())
    encoders.encode_base64(att)

    #Adiciona o cabeçalho no tipo anexo de email
    att.add_header('Content-Disposition','attachment; filename={attach_file}')

    #fecha o arquivo
    attach_file.close()

    #insere no corpo do email
    email_msg.attach(att)

    #todo -------------------- cria a planilha html para uso posterior do bot_whatsapp se preciso
    #f = open('planilha.html','w')
    #f.write(corpo_email)
    #f.close()

    #!-------------------------------------------------------------------------------------------------------------
    #!4 - Envia o email tipo MIME no SERVIDOR SMTP
    #!-------------------------------------------------------------------------------------------------------------
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())
    

    #!Encerra o servidor
    server.quit()

    
    
    

