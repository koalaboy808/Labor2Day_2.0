from sqlalchemy.ext.hybrid import hybrid_property
from app import bcrypt
from flask_bcrypt import generate_password_hash
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
    # username = db.Column(db.String(60), unique=True)
    bestmethod = db.Column(db.String(60), unique=False)
    # password = db.Column(db.String(60), unique=False)
    phone = db.Column(db.String(20), unique=False)
    requests = db.relationship('employer_request', backref='employers',lazy='dynamic')
    username = db.Column(db.String(60), unique=True)
    _password = db.Column(db.String(60))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)

class employer_request(db.Model):
    request_id = db.Column(db.Integer, primary_key=True)
    request_title = db.Column(db.String(120))
    request_description = db.Column(db.String(120))
    request_time = db.Column(db.String(120))
    request_num_ppl = db.Column(db.Integer)
    emp_id = db.Column(db.Integer, db.ForeignKey('employers.employer_id'))

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(60), unique=True)
#     password = db.Column(db.String(60))

#     @hybrid_property
#     def password(self):
#         return self._password

#     @password.setter
#     def _set_password(self, plaintext):
#         self._password = bcrypt.generate_password_hash(plaintext)
    # def __repr__():
    #     return request_title
