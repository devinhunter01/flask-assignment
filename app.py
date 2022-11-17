from flask import Flask, render_template

app = Flask(__name__)

def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

@app.route('/')
def home():
	return render_template('base.html')

@app.route('/user/<name>')
def name(name):
	return f'you are {name}, congrats'

@app.route('/about')
def about():
	return render_template('about.html', about = readDetails('static/about.txt'))
