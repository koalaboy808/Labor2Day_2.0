from flask import render_template, redirect, request, url_for, session, escape, jsonify
from app import app, models, db, bcrypt, login_manager
from flask_bcrypt import generate_password_hash
from flask_login import login_user
import json

@app.route('/')
@app.route('/index')
def index():
	if 'username' in session:
		username = escape(session['username'])
		return render_template('LandingPage.html',name=username)
	else:
		try:
			error=request.args['error']
			error=error[1:len(error)-1]
			return render_template('index.html', error=error)
		except:
			return render_template('index.html')


@app.route('/login/', methods=['POST'])
def login():
	name = request.form['username']
	password = request.form['password']
	# print(name)
	# print("bcrypt")
	# print(models.Employers.query.filter_by(username=name).first_or_404())

	user = models.Employers.query.filter_by(username=name).first_or_404()

	if bcrypt.check_password_hash(user._password,password):
		login_user(user)
		session['username'] = name
		username = escape(session['username'])
		return redirect(url_for('landingpage'))
	else:
		return redirect(url_for('index'))

	return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
	error = json.dumps("Username does not exist")
	# error = escape("Username does not exist")
	return redirect(url_for('index', error=error))

@app.route('/landingpage')
def landingpage():
	if 'username' in session:
		username = escape(session['username'])
		# get_user_id = models.Employers.query.filter_by(username=username)
		# user_id = get_user_id[0].employer_id
		# job_data = models.employer_request.query.filter_by(emp_id=user_id)
		# print(job_data[0].request_title)
		return render_template('LandingPage.html',name=username)
	else:
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
	session['username'] = request.form['username']
	user_name = escape(session['username'])
	return render_template('LandingPage.html',name=user_name)

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
		request_status = "open",
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


# @app.route('/loadlaborercard', methods=['POST'])
# def CreateJobCard():
# 	data = json.loads(request.form.get('data'))
# 	username = data['username']
# 	title_card = data['cardtitle']
# 	descriptiom_card = data['description']
# 	number_card = data['numberofworkers']
# 	time_card = data['timeofjob']
#
# 	get_user_id = models.Employers.query.filter_by(username=username)
# 	user_id = get_user_id[0].employer_id
# 	print(user_id)
#
#
# 	request_table = models.employer_request(
# 		request_title = title_card,
# 		request_description = descriptiom_card,
# 		request_num_ppl = number_card,
# 		request_time = time_card,
# 		request_status = "open",
# 		emp_id = user_id
# 	    # street2 = request.form['street2'],
# 	)
# 	db.session.add(request_table)
# 	db.session.commit()
#
# 	# print(data)
# 	# print(title_card)
# 	# print(descriptiom_card)
# 	# print(time_card)
#
# 	# name = request.form['title_input']
# 	# name = request.form['name']
# 	# print(name)
# 	# name = request.form['name']
# 	# print(name)
# 	print("asdasdasdasdasdasdasdasdsadas")
# 	return 'yes'
# 	# return render_template('LandingPage.html')


@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))

@app.route('/loadjobcards', methods=['POST'])
def loadjobcards():
	jobcards = []
	username = escape(session['username'])
	get_user_id = models.Employers.query.filter_by(username=username)
	user_id = get_user_id[0].employer_id
	job_data = models.employer_request.query.filter_by(emp_id=user_id)

	# print(job_data[1].request_title)
	for jobs in job_data:
		temp={}
		temp["request_title"] = jobs.request_title
		temp["request_description"] = jobs.request_description
		temp["request_time"] = jobs.request_time
		temp["request_num_ppl"] = jobs.request_num_ppl
		# temp.append(jobs.request_description)
		# temp.append(jobs.request_time)
		# temp.append(jobs.request_num_ppl)
		jobcards.append(temp)

	print(jobcards)
	#
	# print(jobs[0])

	# return jsonify(result=jobcards)
	return json.dumps(jobcards)
