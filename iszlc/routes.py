from iszlc import app
from flask import render_template, redirect, url_for, flash, request
from iszlc.models import Doctors
from iszlc.forms import RegisterForm
from iszlc import db

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

#### GLOWNE

@app.route('/iszlc')
def iszlc_page():
    return render_template('iszlc.html')

## LEKI

@app.route('/leki_wyszukaj')
def leki_wyszukaj_page():
    return render_template('leki/wyszukaj.html')

@app.route('/leki_dopisz')
def leki_dopisz_page():
    return render_template('leki/dopisz.html')

## RECEPTY

@app.route('/recepty_wyszukaj')
def recepty_wyszukaj_page():
    return render_template('recepty/wyszukaj.html')

@app.route('/recepty_dopisz')
def recepty_dopisz_page():
    return render_template('recepty/dopisz.html')

@app.route('/recepty_drukuj')
def recepty_drukuj_page():
    return render_template('recepty/drukuj.html')

## PRODUKCJA

## PACJENCI

@app.route('/pacjenci_wyszukaj')
def pacjenci_wyszukaj_page():
    return render_template('pacjenci/wyszukaj.html')

@app.route('/pacjenci_dopisz')
def pacjenci_dopisz_page():
    return render_template('pacjenci/dopisz.html')

## RAPORTY

## SLOWNIKI

@app.route('/slowniki_oddzialy')
def slowniki_oddzialy_page():
    return render_template('modules.html')

@app.route('/slowniki_users')
def slowniki_users_page():
    return render_template('slowniki/users.html')

#### MODULY

@app.route('/moduly')
def modules_page():
    return render_template('slowniki/oddzialy.html')

# --

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

# DODAWANIE

@app.route('/dodaj', methods=['GET', 'POST'])
def add_page():
    form = RegisterForm()
    if form.validate_on_submit():
        doctor_to_create = Doctors(doctor_surname=form.doctor_surname.data,
                                   doctor_name=form.doctor_name.data,
                                   doctor_nr=form.doctor_nr.data)
        db.session.add(doctor_to_create)
        db.session.commit()
        flash(f"Doktor dodany pomyslnie!", category='success')
        return redirect(url_for('iszlc_page'))

    if form.errors != {}: #Jesli nie ma bledow z validatora
        for err_msg in form.errors.values():
            flash(f'Bląd dodania doktora: {err_msg}', category='danger')

    return render_template('add.html', form=form)



## PDF

from flask import render_template, make_response
import pdfkit

# @app.route('/<name>/<location>') #http://127.0.0.1:5000/Piotr/Sosnowka
# def pdf_page(name, location):
#    rendered = render_template('pdf.html')
#    pdf = pdfkit.from_string(rendered, False)

#    response = make_response(pdf)
#    response.headers['Content-Type'] = 'application/pdf'
#    response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'

#    return response