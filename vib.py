from flask import Flask, request, redirect, render_template
from database import *
import random

app = Flask(__name__)
 
@app.route('/')
def index():
	 # add_article("Your next house could save the planet","https://www.israel21c.org/topic/village-in-a-box/")
	 # add_article("Israeli Sustainability Initiative To Pilot Village-In-A-Box With Its Own Water, Food, Energy Systems","https://nocamels.com/2019/07/israeli-sustainability-pilot-village-in-a-box-water-food-energy/")
	 # add_article("Village-in-a-box:","https://www.mako.co.il/nexter-high-tech/Article-ab50bcaf5d10a61006.htm")
	 # add_article("Village-in-a-box CHIVAS THE VENTURE ","https://www.foodis.co.il/village-in-a-box-chivas-the-venture/")
	 everything = query_all_articles()
	 random_list = []
	 values = ['Village','Community','Zero Emissions','Sustainability']
	 for i in range(3):
		random_list.append(everything.pop(random.randint(0,len(everything)-1)))

	 return render_template('index.html', random_list = random_list, values = values)

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
