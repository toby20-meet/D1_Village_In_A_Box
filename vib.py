from flask import Flask, request, redirect, render_template
from database import *
import random
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'theybotman@gmail.com'
app.config['MAIL_PASSWORD'] = 's0undc00kie'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
 
@app.route('/')
def index():
	 # add_article("Your next house could save the planet","https://www.israel21c.org/topic/village-in-a-box/")
	 # add_article("Israeli Sustainability Initiative To Pilot Village-In-A-Box With Its Own Water, Food, Energy Systems","https://nocamels.com/2019/07/israeli-sustainability-pilot-village-in-a-box-water-food-energy/")
	 # add_article("Village-in-a-box:","https://www.mako.co.il/nexter-high-tech/Article-ab50bcaf5d10a61006.htm")
	 # add_article("Village-in-a-box CHIVAS THE VENTURE ","https://www.foodis.co.il/village-in-a-box-chivas-the-venture/")
	 everything = query_all_articles()
	 random_list = []
	 for i in range(3):
	 	 random_list.append(everything.pop(random.randint(0,len(everything)-1)))
	 return render_template('index.html', random_list = random_list)

@app.route('/join')
def join():
	return render_template('join.html')

@app.route('/team')
def team():
	return render_template('about.html')

@app.route('/contact',methods = ['GET','POST'])
def contact():
	 if request.method == 'POST':
	 	msg = Message(request.form['message'],
        sender=request.form['address'],
        recipients=["theybotman@gmail.com"])
		mail.send(msg)
	 return render_template('contact.html')

if __name__ == '__main__':
	app.run(debug = True)
