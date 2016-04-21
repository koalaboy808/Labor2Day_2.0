from flask import render_template, redirect, request, url_for
from flask_login import login_user
from app import app, models, db
from flask_bcrypt import generate_password_hash
import json

@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
	# if request.method =="POST":
	# 	if request.form['submit'] == "Login":
	# 		return redirect('/signup')
	return render_template('index.html')


@app.route('/landingpage/', methods=['POST'])
def landing():
	name = request.form['username']
	# print(name)
	user = models.Employers.query.filter_by(username=name).first_or_404()
	if user.is_correct_password(name):
		print(user.is_correct_password(name))
		login_user(user)

		return render_template('LandingPage.html',name=name)
	else:
		print(user)
		print(user.is_correct_password(name))
		print("wrong")
		return render_template('index.html')
	# return render_template('LandingPage.html',name=name)


@app.route('/signup')
def signup():
	return render_template('SignUp.html')


@app.route('/employer/', methods=['POST'])
def CreateEmployer():
	name = request.form['username']
	employer = models.Employers(
	# employer = models.Employers(
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
	    _password = generate_password_hash(request.form['password'], 12),
	    phone = request.form['phone']
	)
	print(name)
	db.session.add(employer)
	db.session.commit()
	return render_template('LandingPage.html',name=name)
	# return redirect(url_for('landingpage', name=name))

@app.route('/CreateJobCard', methods=['POST'])
def CreateJobCard():
	data = json.loads(request.form.get('data'))
	title_card = data['cardtitle']
	descriptiom_card = data['description']
	number_card = data['numberofworkers']
	time_card = data['timeofjob']

	request_table = models.employer_request(
		request_title = title_card,
		request_description = descriptiom_card,
		request_num_ppl = number_card,
		request_time = time_card,
		emp_id = '1'
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
