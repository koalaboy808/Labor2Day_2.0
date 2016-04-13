from app import db

class Employers(db.Model):
    employer_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(60), unique=False)
    mname = db.Column(db.String(60), unique=False)
    lname = db.Column(db.String(60), unique=False)
    street1 = db.Column(db.String(60), unique=False)
    street2 = db.Column(db.String(60), unique=False)
    city = db.Column(db.String(120), unique=False)
    state = db.Column(db.String(60), unique=False)
    zipcode = db.Column(db.Integer, unique=False)
    email = db.Column(db.String(120), unique=False)
    username = db.Column(db.String(60), unique=False)
    bestmethod = db.Column(db.String(60), unique=False)
    password = db.Column(db.String(60), unique=False)
    phone = db.Column(db.String(20), unique=False)
    requests = db.relationship('employer_request', backref='employers',lazy='dynamic')

class employer_request(db.Model):
    request_id = db.Column(db.Integer, primary_key=True)
    request_title = db.Column(db.String(120))
    request_description = db.Column(db.String(120))
    request_time = db.Column(db.String(120))
    request_num_ppl = db.Column(db.Integer)
    emp_id = db.Column(db.Integer, db.ForeignKey('employers.employer_id'))

    # def __repr__():
    #     return request_title
