from flask import Flask, render_template, request, flash
from os import listdir
import send_email 
import v6_selenium
#from gevent.pyswgi import WSGIServer

app = Flask(__name__, template_folder='template', static_folder='static')
app.secret_key="asd"

name_fsite = ''
sof_fsite = ''
email_fsite = ''
dateS_fsite = ''
dateE_fsite = ''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST','GET'])
def search():
    flash('Dados inserido, aguarde que logo será enviado o resultado')
    if str(request.form['dateS_input']) == '' or str(request.form['dateE_input']) == '':
        return render_template("falha.html")
    if str(request.form['sof_input']) == '' or str(request.form['email_input']) == '':
        return render_template("falha.html")
    name_fsite = str(request.form['name_input'])
    email_fsite = str(request.form['email_input'])
    sof_fsite = str(request.form['sof_input'])
    replace_dS_fsite = str(request_form['dateS_input']).split("-")
    dateS_fsite = replace_dS_fsite[1] + replace_dS_fsite[2] + replace_dS_fsite[0]
    replace_dE_fsite = str(request_form['dateE_input']).split("-")
    dateE_fsite = replace_dE_fsite[1] + replace_dE_fsite[2] + replace_dE_fsite[0]
    list_email = []
    list_email.append(email_fsite)
    list_form_fill = []
    list_form_fill = v6_selenium.get_data(sof_fsite, dateS_fsite, dateE_fsite)
    send_email.send(list_email) #send_form
    return render_template("pesquisa.html")

#@app.route('/')
#def run_script():
#    file = open(r'v6_selenium.py', 'r').read()
#    return exec(file)
        
if __name__=="__main__":
    app.run(debug=True)
