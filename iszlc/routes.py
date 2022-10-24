from iszlc import app
from flask import render_template, redirect, url_for, flash, request
from iszlc.models import Leki, Pacjenci, Uzytkownicy
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
    leki = Leki.query.all()
    return render_template('leki/wyszukaj.html', Leki=leki)

@app.route('/leki_dopisz', methods=['GET', 'POST'])
def leki_dopisz_page():
    form = RegisterForm()
    if form.validate_on_submit():
        leki_to_create = Leki(ean=form.leki_ean.data,
                            nazwa_handlowa=form.leki_nazwa_handlowa.data,
                            nazwa_miedzynarodowa=form.leki_nazwa_miedzynarodowa.data,
                            )
        db.session.add(leki_to_create)
        db.session.commit()
        flash(f"Lek dodany pomyslnie!", category='success')
        return redirect(url_for('iszlc_page'))

    if form.errors != {}: #Jesli nie ma bledow z validatora
        for err_msg in form.errors.values():
            flash(f'Bląd dodania leku: {err_msg}', category='danger')

    return render_template('leki/dopisz.html', form=form)

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

@app.route('/pacjenci_dopisz', methods=['GET', 'POST'])
def pacjenci_dopisz_page():
    form = RegisterForm()
    if form.validate_on_submit():
        pacjent_to_create = Pacjenci(nazwisko=form.lek_ean.data,
                            pierwsze_imie=form.lek_nazwa_handlowa.data,
                            drugie_imie=form.lek_nazwa_miedzynarodowa.data,
                            pesel=form.lek_ean.data,
                            data_urodzenia=form.lek_ean.data,
                            badanie=form.lek_ean.data,
                            nr_w_badaniu=form.lek_ean.data,
                            )
        db.session.add(pacjent_to_create)
        db.session.commit()
        flash(f"Pacjent dopisany pomyslnie!", category='success')
        return redirect(url_for('iszlc_page'))

    if form.errors != {}: #Jesli nie ma bledow z validatora
        for err_msg in form.errors.values():
            flash(f'Bląd dopisywania pacjenta: {err_msg}', category='danger')

    return render_template('pacjenci/dopisz.html', form=form)

## RAPORTY

## SLOWNIKI

@app.route('/slowniki_oddzialy')
def slowniki_oddzialy_page():
    return render_template('modules.html')

@app.route('/add_dodaj_uzytkownika', methods=['GET', 'POST'])
def add_dodaj_uzytkownika_page():
    form = RegisterForm()
    if form.validate_on_submit():
        uzytkownik_to_create = Uzytkownicy(nazwisko=form.nazwisko.data,
                                imie=form.imie.data,
                                pwz=form.pwz.data,
                                tytul_naukowy=form.tytul_naukowy.data,
                                uprawnienia=form.uprawnienia.data,
                                haslo=form.haslo.data)
        db.session.add(uzytkownik_to_create)
        db.session.commit()
        flash(f"Użytkownik dodany pomyslnie!", category='success')
        return redirect(url_for('slowniki_uzytkownicy_page'))

    if form.errors != {}: #Jesli nie ma bledow z validatora
        for err_msg in form.errors.values():
            flash(f'Bląd dodania użytkownika: {err_msg}', category='danger')

    return render_template('add/dodaj_uzytkownika.html', form=form)

@app.route('/slowniki_uzytkownicy')
def slowniki_uzytkownicy_page():
    user = Uzytkownicy.query.all()
    return render_template('slowniki/uzytkownicy.html', Uzytkownicy=user)

@app.route('/slowniki_wlasciciel')
def slowniki_wlasciciel_page():
    return render_template('slowniki/owner.html')  

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

#@app.route('/doktorzy')
#def doktorzy_page():
 #   doctor = Doctors.query.all()
 #   return render_template('doktorzy.html', Doctors=doctor)

# DODAWANIE

#@app.route('/dodaj_doktor', methods=['GET', 'POST'])
#def add_doctor_page():
#    form = RegisterForm()
#    if form.validate_on_submit():
 #       doctor_to_create = Doctors(nazwisko=form.nazwisko.data,
 #                                  imie=form.imie.data,
 #                                  nr=form.nr.data)
#        db.session.add(doctor_to_create)
#       db.session.commit()
#        flash(f"Doktor dodany pomyslnie!", category='success')
 #       return redirect(url_for('iszlc_page'))

 #   if form.errors != {}: #Jesli nie ma bledow z validatora
 #       for err_msg in form.errors.values():
 #           flash(f'Bląd dodania doktora: {err_msg}', category='danger')
#
 #   return render_template('add/add_doctor.html', form=form)




## PDF

#from flask import render_template, make_response
#import pdfkit

# @app.route('/<name>/<location>') #http://127.0.0.1:5000/Piotr/Sosnowka
# def pdf_page(name, location):
#    rendered = render_template('pdf.html')
#    pdf = pdfkit.from_string(rendered, False)

#    response = make_response(pdf)
#    response.headers['Content-Type'] = 'application/pdf'
#    response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'

#    return respone