from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page Route'


@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'


@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text


#from http.server import BaseHTTPRequestHandler
 
#class handler(BaseHTTPRequestHandler):
 
    #def do_GET(self):
        #self.send_response(200)
        #self.send_header('Content-type','text/plain')
        #self.end_headers()
        #self.wfile.write('Hello, world!'.encode('utf-8'))
        #return
