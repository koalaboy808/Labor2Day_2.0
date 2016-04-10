from flask import render_template, redirect, request
from app import app, models, db

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


@app.route('/employer/', methods=['POST'])
def CreateEmployer():
	name = request.form['username']
	employer = models.Employers(
		fname = request.form['first_name'],
		mname = request.form['middle_name'],
		lname = request.form['last_name'],
		street1 = request.form['street1'],
	    street2 = request.form['street2'],
	    city = request.form['city'],
	    state = request.form['state'],
	    zipcode = request.form['zipcode'],
	    email = request.form['email'],
	    username = request.form['username'],
	    bestmethod = request.form['demo-priority'],
	    password = request.form['password'],
	    phone = request.form['phone']
	)
	print(name)
	db.session.add(employer)
	db.session.commit()
	return render_template('LandingPage.html',name=name)
