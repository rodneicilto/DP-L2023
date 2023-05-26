from flask import Flask, render_template, request
from os import listdir
app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

    @app.route('/', methods= ['POST', 'GET'])
    def form_home():
        input_name = request.form['name_input']
        input_email = request.form['email_input']
        input_sof = request.form['sof_input']
        input_startD = request.form['dateS_input']
        input_endD = request.form['dateE_input']
        if request.method == 'POST':
            f.write(str(input_name,input_email,input_sof,input_startD,input_endD))
            return render_template("index.html", nopol=input_name)

@app.route('/about')
def about():
    return 'About Page Route'

@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'

@app.route('/contact')
def contact():
    return 'Contact Page Route'

@app.route('/api/src')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text
        
if __name__=="__main__":
    app.run(debug=True)
