from flask import render_template, redirect, request
from app import app, models, db

@app.route('/')
def index():
    return render_template('index.html')
