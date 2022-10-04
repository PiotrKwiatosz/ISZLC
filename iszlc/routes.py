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

#### GLOWNE

# @app.route('/login')
# def login_page():
#   return render_template('login.html')

@app.route('/iszlc')
def iszlc_page():
    return render_template('iszlc.html')

## LEKI

@app.route('/leki_wyszukaj')
def leki_wyszukaj_page():
    return render_template('leki/wyszukaj.html')

## RECEPTY

@app.route('/recepty_wyszukaj')
def recepty_wyszukaj_page():
    return render_template('recepty/wyszukaj.html')

## PRODUKCJA

@app.route('/produkcja-wyszukaj')
def produkcja_wyszukaj_page():
    return render_template('produkcja/wyszukaj.html')

## PACJENCI

@app.route('/pacjenci-wyszukaj')
def pacjenci_wyszukaj_page():
    return render_template('pacjenci/wyszukaj.html')

## RAPORTY

## SLOWNIKI


#### MODULY

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
