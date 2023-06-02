from flask import Flask, render_template, request
from os import listdir
from send_email import send 
#from gevent.pyswgi import WSGIServer

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['post'])
def contact():
    if request.method == 'post': 
        print(request.form)
        print(request.form['name_input'])
        print(request.form['email_input'])
        print(request.form['sof_input'])
        print(request.form['dateS_input'])
        print(request.form['dateE_input'])
        send_email.send('name_input')
    return "OK"

#@app.route('/')
#def run_script():
#    file = open(r'v6_selenium.py', 'r').read()
#    return exec(file)
        
if __name__=="__main__":
    app.run(debug=True)
