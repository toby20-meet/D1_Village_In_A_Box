from flask import Flask, request, redirect, render_template

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join')
def join():
    return 'Hello, World'

@app.route('/team')
def team():
    return 'Hello, World'

@app.route('/about')
def about():
    return 'Hello, World'

if __name__ == '__main__':
	app.run(debug = True)
