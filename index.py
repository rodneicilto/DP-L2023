from flask import Flask, render_template, request
from os import listdir
#from gevent.pyswgi import WSGIServer

app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['post', 'get'])
def form_home():
    if request.method == 'post':
<<<<<<< HEAD
        with open('nopol_1.txt', 'w') as f:
            f.write(str(input_name))
    return render_template("index.html", nopol_1=input_name)

@app.route('/about')
def about():
    return 'About Page Route'

@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'

@app.route('/contact')
def contact():
    return 'Contact Page Route'
        print(request.form)
        print(request.form['name_input'])
        print(request.form['email_input'])
        print(request.form['sof_input'])
        print(request.form['dateS_input'])
        print(request.form['dateE_input'])
    return request.form['name_input'] + request.form['email_input']

@app.route('/api/src')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text
        
if __name__=="__main__":
    app.run(debug=True)
