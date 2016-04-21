from app import db, bcrypt

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
    _password = db.Column(db.String(60), unique=False)
    phone = db.Column(db.String(20), unique=False)
    requests = db.relationship('employer_request', backref='employers',lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.employer_id)  # python 2
        except NameError:
            return str(self.employer_id)  # python 3

class employer_request(db.Model):
    request_id = db.Column(db.Integer, primary_key=True)
    request_title = db.Column(db.String(120))
    request_description = db.Column(db.String(120))
    request_time = db.Column(db.String(120))
    request_num_ppl = db.Column(db.Integer)
    emp_id = db.Column(db.Integer, db.ForeignKey('employers.employer_id'))

# class fulfillment(db.Model):
#     fulfillment_id = db.Column(db.Integer, primary_key=True)
#     fulfillment_req_id = db.Column(db.Integer)
#     laborers = db.relationship('laborer', backref='fulfillment',lazy='dynamic')


class laborer(db.Model):
    laborer_id = db.Column(db.Integer, primary_key=True)
    laborer_first_name = db.Column(db.String(120))
    laborer_last_name = db.Column(db.String(100))
    laborer_skills = db.Column(db.String(50))
    laborer_phone_num = db.Column(db.Integer)
    # fulfl_id = db.Column(db.Integer, db.ForeignKey('fulfillment.fulfillment_id'))

    # def __repr__():
    #     return request_title
