from flask import Flask, render_template, request
from os import listdir
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
    return request.form['name_input'] + request.form['email_input']

#@app.route('/api/')
#def run_script():
#    file = open(os.path.expanduser(v6_selenium.py)).read()
#    return exec(file)
        
if __name__=="__main__":
    app.run(debug=True)
