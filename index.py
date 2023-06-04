from flask import Flask, render_template, request, flash
from os import listdir
from send_email import send 
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
    #dateS_fsite = 
    #dateE_fsite
    #str(request.form)
    #print(request.form['name_input'])
    #print(request.form['email_input'])
    #print(request.form['sof_input'])
    #print(request.form['dateS_input'])
    #print(request.form['dateE_input'])
    list_email = []
    list_email.append(email_site)
     #list_form_fill = []
     #list_form = v6_selenium.web_scraping(name_fsite, email_fsite, sof_fsite, dateS_fsite, dateE_fsite)
     #send_form = v6_selenium.envia_file(list_form[1])
    send_email.send(list_emal) #send_form
    return render_template ("pesquisa.html")

#@app.route('/')
#def run_script():
#    file = open(r'v6_selenium.py', 'r').read()
#    return exec(file)
        
if __name__=="__main__":
    app.run(debug=True)
