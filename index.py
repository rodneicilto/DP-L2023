from flask import Flask, render_template, request


app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods= ['POST'])
def form():
    name = request.form['name_input']
    email = request.form['email_input']
    sftw = request.form['sftw_input']
    dateS = request.form['dateS_input']
    dateE = request.form['dataE_input']

def save(text,filepath='test.txt'):
    with open("test.txt", "w") as f:
        f.write(text)
app.run()




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
