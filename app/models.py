from app import db

class Employers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
