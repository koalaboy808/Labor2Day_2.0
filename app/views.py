from flask import render_template, redirect, request, url_for
from app import app, models, db, bcrypt, login_manager
from flask_bcrypt import generate_password_hash
from flask_login import login_user
import json

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
	password = request.form['password']
	print(name)
	user = models.Employers.query.filter_by(username=name).first_or_404()
	if bcrypt.check_password_hash(user._password,password):
		login_user(user)
		return render_template('LandingPage.html',name=name)
	else:
		return redirect(url_for('index'))

	return render_template('index.html')


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
	    _password = generate_password_hash(request.form['password'],12),
	    phone = request.form['phone']
	)
	print(name)
	db.session.add(employer)
	db.session.commit()
	return render_template('LandingPage.html',name=name)

@app.route('/CreateJobCard', methods=['POST'])
def CreateJobCard():
	data = json.loads(request.form.get('data'))
	username = data['username']
	title_card = data['cardtitle']
	descriptiom_card = data['description']
	number_card = data['numberofworkers']
	time_card = data['timeofjob']

	get_user_id = models.Employers.query.filter_by(username=username)
	user_id = get_user_id[0].employer_id
	print(user_id)


	request_table = models.employer_request(
		request_title = title_card,
		request_description = descriptiom_card,
		request_num_ppl = number_card,
		request_time = time_card,
		emp_id = user_id
	    # street2 = request.form['street2'],
	)
	db.session.add(request_table)
	db.session.commit()

	# print(data)
	# print(title_card)
	# print(descriptiom_card)
	# print(time_card)

	# name = request.form['title_input']
	# name = request.form['name']
	# print(name)
	# name = request.form['name']
	# print(name)
	print("asdasdasdasdasdasdasdasdsadas")
	return 'yes'
	# return render_template('LandingPage.html')
