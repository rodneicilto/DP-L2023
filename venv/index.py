from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/html/index.html')
if __name__ == '__main__':
    app.run()

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
