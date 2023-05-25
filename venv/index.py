from flask import Flask, render_template


app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/html/about')
def about():
    return 'About Page Route'

@app.route('/html/portfolio')
def portfolio():
    return 'Portfolio Page Route'

@app.route('/html/contact')
def contact():
    return 'Contact Page Route'

@app.route('/api/src')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text
