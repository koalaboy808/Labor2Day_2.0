from flask import render_template, redirect, request
from app import app

@app.route('/')
@app.route('/index')
def index():
	# if request.method =="POST":
	# 	if request.form['submit'] == "Login":
	# 		return redirect('/signup')
	return render_template('index.html')


@app.route('/landingpage/', methods=['POST'])
def landing():
	name = request.form['username']
	print(name)
	return render_template('LandingPage.html',name=name)


@app.route('/signup')
def signup():
	return render_template('SignUp.html')
