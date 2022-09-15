from iszlc import app
from flask import render_template, redirect, url_for, flash
from iszlc.models import Doctors
from iszlc.forms import RegisterForm
from iszlc import db

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/iszlc')
def iszlc_page():
    doktor = Doctors.query.all()
    return render_template('iszlc.html', Doctors=doktor)

@app.route('/dodaj', methods=['GET', 'POST'])
def add_page():
    form = RegisterForm()
    if form.validate_on_submit():
        doktor_to_create = Doctors(doctor_name=form.doctor_name.data,
                                   doctor_surname=form.doctor_surname.data,
                                   doctor_nr=form.doctor_nr.data)
        db.session.add(doktor_to_create)
        db.session.commit()
        flash(f"Doktor dodany pomyslnie!", category='success')
        return redirect(url_for('iszlc_page'))

    if form.errors != {}: #Jesli nie ma bledow z validatora
        for err_msg in form.errors.values():
            flash(f'Blad tworzenia uzytkownika: {err_msg}', category='danger')

    return render_template('add.html', form=form)