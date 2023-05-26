from flask import Flask, render_template, request


app = Flask(__name__, template_folder='template', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods= ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)

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
