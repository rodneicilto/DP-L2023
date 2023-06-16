from flask import Flask, render_template, request, flash, redirect
from datetime import datetime, date, timedelta
from os import listdir
import send_email 
import v6_selenium

app = Flask(__name__, template_folder='template', static_folder='static')
app.secret_key="asd"

name_fsite = ''
sof_fsite = ''
email_fsite = ''
dateS_fsite_T = ''
dateS_fsite = ''
dateE_fsite_T = ''
dateE_fsite = ''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST','GET'])
def research():
    #Dados recebidos do formulario
    flash('Dados inserido, aguarde que logo será enviado o resultado')
    name_fsite = str(request.form['name_input'])
    email_fsite = str(request.form['email_input'])
    sof_fsite = str(request.form['sof_input'])
    #Conversão da data inicio para efetuar a soma dos periodos
    dateS_fsite_T = str(request.form['dateS_input'])
    replace_Test = dateS_fsite_T
    date_object_S = datetime.strptime(replace_Test, '%Y-%m-%d').date()
    dateE_fsite_T = int(request.form['dateE_input'])
    #Remoção do digito '-' para '/' e alteração do posicionamento do ano 
    replace_fsite_E = (date_object_S + timedelta(days=dateE_fsite_T))
    replace_fsite = str(request.form['dateS_input']).split("-")
    dateS_fsite = replace_fsite[1] + '/' + replace_fsite[2] + '/' + replace_fsite[0]
    replace_fconvert = str(replace_fsite_E).split("-")
    dateE_fsite = replace_fconvert[1] + '/' + replace_fconvert[2] + '/' + replace_fconvert[0]
    #Envio das informações para o processo de webscraping 
    list_form_fill = []
    list_form_fill = v6_selenium.web_scraping(sof_fsite, dateS_fsite, dateE_fsite, name_fsite, email_fsite)
    #Envio das informações coletadas no webscraping por email
    send_email_fill = []
    send_email_fill = send_email.send(email_fsite, name_fsite)
    return render_template('search.html', results=request.form)

#@app.route('/')
#def run_script():
#    file = open(r'v6_selenium.py', 'r').read()
#    return exec(file)
        
if __name__=="__main__":
    app.run(debug=True)
