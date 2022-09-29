from urllib import request
from iszlc import app
from flask import render_template, redirect, url_for, flash, request
from iszlc.models import Doctors
from iszlc.forms import RegisterForm
from iszlc import db

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/moduly')
def iszlc_page():
    return render_template('iszlc.html')

## MODULY

@app.route('/farmaceuta')
def farm_page():
    return render_template('farm.html')

@app.route('/pielegniarki')
def nurse_page():
    return render_template('nurse.html')

@app.route('/doktorzy')
def doktorzy_page():
    doctor = Doctors.query.all()
    return render_template('doktorzy.html', Doctors=doctor)

## DODAWANIE

@app.route('/dodaj', methods=['GET', 'POST'])
def add_page():
    form = RegisterForm()
    if form.validate_on_submit():
#    if request.method == "POST":
        doctor_to_create = Doctors(doctor_surname=form.doctor_surname.data,
                                   doctor_name=form.doctor_name.data,
                                   doctor_nr=form.doctor_nr.data)
        db.session.add(doctor_to_create)
        db.session.commit()
        flash(f"Doktor dodany pomyslnie!", category='success')
        return redirect(url_for('iszlc_page'))

    if form.errors != {}: #Jesli nie ma bledow z validatora
        for err_msg in form.errors.values():
            flash(f'Blad dodania doktora: {err_msg}', category='danger')

    return render_template('add.html', form=form)