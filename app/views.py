from flask import render_template, redirect, request, url_for, session, escape, jsonify
from app import app, models, db, bcrypt, login_manager
from flask_bcrypt import generate_password_hash
from flask_login import login_user
from twilio.rest import TwilioRestClient
import json

twilioNum = "+12014742384"
account_sid = "AC5db2f903ee4a9ad48869db297e2a8acd"
auth_token = "868a8ae2f1377d3a421c2d7237d52fdc"

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
	return redirect(url_for('index', error=error))

@app.route('/landingpage')
def landingpage():
	if 'username' in session:
		username = escape(session['username'])
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
	db.session.add(employer)
	db.session.commit()
	session['username'] = request.form['username']
	user_name = escape(session['username'])
	return render_template('LandingPage.html',name=user_name)

@app.route('/CreateJobCard', methods=['POST'])
def CreateJobCard():
	data = json.loads(request.form.get('data'))
	username = data['username'].lower()
	title_card = data['cardtitle']
	descriptiom_card = data['description']
	number_card = data['numberofworkers']
	time_card = data['timeofjob']

	get_user_id = models.Employers.query.filter_by(username=username)
	user_id = get_user_id[0].employer_id

	request_table = models.employer_request(
		request_title = title_card,
		request_description = descriptiom_card,
		request_num_ppl = number_card,
		request_time = time_card,
		request_status = "open",
		emp_id = user_id
	)
	db.session.add(request_table)
	db.session.commit()


	get_request_id = models.employer_request.query.filter_by(request_title=title_card)
	_request_id = get_request_id[0].request_id

	return json.dumps(_request_id)



@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))

@app.route('/profile')
def profile():
	username = escape(session['username'])
	return render_template('profile.html', name=username)



@app.route('/loadjobcards', methods=['POST'])
def loadjobcards():
	jobcards = []
	username = escape(session['username'])
	get_user_id = models.Employers.query.filter_by(username=username)
	user_id = get_user_id[0].employer_id
	job_data = models.employer_request.query.filter_by(emp_id=user_id)


	for jobs in job_data:
		temp={}
		if jobs.request_status == "open":
			temp["request_id"] = jobs.request_id
			temp["request_title"] = jobs.request_title
			temp["request_description"] = jobs.request_description
			temp["request_time"] = jobs.request_time
			temp["request_num_ppl"] = jobs.request_num_ppl
			laborer_array = []
			laborers = models.fulfillment.query.filter_by(fulfillment_request_id=jobs.request_id)
			for laborer_data in laborers:
				laborer_name = models.laborer.query.filter_by(laborer_id=laborer_data.fulfillment_laborer_id)
				temp_name = {}
				for names in laborer_name:
					temp_name["id"] = names.laborer_id
					temp_name["name"] = names.laborer_name
					laborer_array.append(temp_name)


			temp["laborer_data"] = laborer_array
			jobcards.append(temp)


	return json.dumps(jobcards)

@app.route('/loadlaborers', methods=['POST'])
def loadlaborers():
	laborers = []
	laborer_data = models.laborer.query.filter_by(laborer_availability="y")

	for laborer in laborer_data:
		temp={}
		temp["laborer_id"] = laborer.laborer_id
		temp["laborer_name"] = laborer.laborer_name
		temp["laborer_phone_num"] = laborer.laborer_phone_num
		temp["laborer_availability"] = laborer.laborer_availability
		temp["laborer_skill"] = laborer.laborer_skill

		laborers.append(temp)

	return json.dumps(laborers)

@app.route('/Createfulfillment', methods=['POST'])
def Createfulfillment():
	i=0
	data = json.loads(request.form.get('data'))
	fulfillment_request_id = data['request_id']
	fulfillment_laborer_id = data['laborer_id']

	num_workers = models.employer_request.query.filter_by(request_id=fulfillment_request_id)
	num_of_workers = num_workers[0].request_num_ppl


	count_workers = models.fulfillment.query.filter_by(fulfillment_request_id=fulfillment_request_id)
	for count in count_workers:
		i=i+1

	if i < num_of_workers:

		fulfillment_table = models.fulfillment(
			fulfillment_request_id = fulfillment_request_id,
			fulfillment_laborer_id = fulfillment_laborer_id,
			fulfillment_status = "pending"
		)

		db.session.add(fulfillment_table)

		get_laborer = models.laborer.query.filter_by(laborer_id=fulfillment_laborer_id)
		get_laborer[0].laborer_availability = "n"

		number = get_laborer[0].laborer_phone_num
		client = TwilioRestClient(account_sid, auth_token)
		message = client.messages.create(to=number, from_=twilioNum, body="We have found a job for you. Reply Yes to accept and No to decline.")
		db.session.commit()

		return "love"
	else:
		return "no"

@app.route('/jobcard_done', methods=['POST'])
def jobcard_done():
	print("lalalalalals")


	data = json.loads(request.form.get('data'))
	_request_id = int(data['request_id'].encode('ascii','ignore'))
	_list_of_ids = (data['list_of_ids'])



	get_employer_request = models.employer_request.query.filter_by(request_id=_request_id)
	get_employer_request[0].request_status = "closed"

	x = models.fulfillment.query.filter_by(fulfillment_request_id=_request_id).delete()

	for _id in _list_of_ids:
		get_laborer = models.laborer.query.filter_by(laborer_id=_id)
		get_laborer[0].laborer_availability = "y"


	db.session.commit()

	return "fuck functions and returns"

@app.route('/profile_cards', methods=['POST'])
def profile_cards():
	jobcards = []
	username = escape(session['username'])
	get_user_id = models.Employers.query.filter_by(username=username)
	user_id = get_user_id[0].employer_id
	job_data = models.employer_request.query.filter_by(emp_id=user_id)

	counter =0
	for jobs in job_data:
		counter+=1
		temp={}
		if jobs.request_status == "closed":
			temp["request_id"] = jobs.request_id
			temp["request_title"] = jobs.request_title
			temp["request_description"] = jobs.request_description
			temp["request_time"] = jobs.request_time
			temp["request_num_ppl"] = jobs.request_num_ppl
			laborer_array = []
			laborers = models.fulfillment.query.filter_by(fulfillment_request_id=jobs.request_id)
			for laborer_data in laborers:
				laborer_name = models.laborer.query.filter_by(laborer_id=laborer_data.fulfillment_laborer_id)
				temp_name = {}
				for names in laborer_name:
					temp_name["id"] = names.laborer_id
					temp_name["name"] = names.laborer_name
					laborer_array.append(temp_name)

			temp["laborer_data"] = laborer_array
			jobcards.append(temp)

	return json.dumps(jobcards)

@app.route('/removelaborer', methods=['POST'])
def removelaborer():
	data = json.loads(request.form.get('data'))
	_lab_id = int(data['laborer_id'].encode('ascii','ignore'))
	_request_id = int(data['request_id'].encode('ascii','ignore'))
	x = models.fulfillment.query.filter_by(fulfillment_laborer_id=_lab_id).delete()
	get_laborer = models.laborer.query.filter_by(laborer_id=_lab_id)
	get_laborer[0].laborer_availability = "y"
	db.session.commit()

	return "love once more"
