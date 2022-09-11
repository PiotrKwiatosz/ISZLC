from iszlc import app
from flask import render_template, redirect, url_for, flash
from iszlc.models import Doctors
from iszlc import db

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/iszlc')
def iszlc_page():
    doktor = Doctors.query.all()
    return render_template('iszlc.html', Doctors=doktor)