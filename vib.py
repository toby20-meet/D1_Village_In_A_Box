from flask import Flask, request, redirect, render_template
from database import *
import random

app = Flask(__name__)
 
@app.route('/')
def index():
	 add_article('hi', 'https://www.wikipedia.org/')
	 add_article('bye', 'https://www.google.com/')
	 add_article('ayy', 'https://www.youtube.com/')
	 everything = query_all_articles()
	 print(len(everything))
	 random_list = []
	 for i in range(3):
		random_list.append(everything.pop(random.randint(0,len(everything))))

	 return render_template('index.html', random_list = random_list)

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
