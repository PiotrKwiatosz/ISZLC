from distutils.command.build_scripts import first_line_re
from iszlc import app
from flask import render_template, redirect, url_for, flash, request
from iszlc.models import Leki, Pacjenci, Uzytkownicy, Owners, Oddzialy
from iszlc.forms import RegisterForm, RegisterUserForm, RegisterDrugForm
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
    lek = Leki.query.all()
    return render_template('leki/wyszukaj.html', Leki=lek)

@app.route('/dodaj_leki', methods=['GET', 'POST'])
def dodaj_leki_page():
    form = RegisterDrugForm()
    if form.validate_on_submit():
        lek_to_create = Leki(ean=form.ean.data,
                            nazwa_handlowa=form.nazwa_handlowa.data,
                            nazwa_miedzynarodowa=form.nazwa_miedzynarodowa.data,
                            )
        db.session.add(lek_to_create)
        db.session.commit()
        flash(f"Lek dodany pomyslnie!", category='success')
        return redirect(url_for('leki_wyszukaj_page'))

    if form.errors != {}: #Jesli nie ma bledow z validatora
        for err_msg in form.errors.values():
            flash(f'Bląd dodania leku: {err_msg}', category='danger')

    return render_template('dodaj/leki.html', form=form)

@app.route('/leki_dopisz')
def leki_dopisz_page():
    return render_template('leki/dopisz.html')

@app.route('/leki_pokaz')
def leki_pokaz_page():
    lek = Leki.query.filter_by(id_lek=1)
    return render_template('leki/pokaz.html', Leki=lek)

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

@app.route('/dodaj_pacjenta', methods=['GET', 'POST'])
def dodaj_pacjenta_page():
    form = RegisterForm()
    if form.validate_on_submit():
        pacjent_to_create = Pacjenci(nazwisko=form.nazwisko.data,
                                    pierwsze_imie=form.pierwsze_imie.data,
                                    drugie_imie=form.drugie_imie.data,
                                    pesel=form.pesel.data,
                                    data_urodzenia=form.data_urodzenia.data,
                                    badanie=form.badanie.data,
                                    nr_w_badaniu=form.nr_w_badaniu.data,
                                    )
        db.session.add(pacjent_to_create)
        db.session.commit()
        flash(f"Pacjent dopisany pomyslnie!", category='success')
        return redirect(url_for('iszlc_page'))

    if form.errors != {}: #Jesli nie ma bledow z validatora
        for err_msg in form.errors.values():
            flash(f'Bląd dopisywania pacjenta: {err_msg}', category='danger')

    return render_template('dodaj/pacjenta.html', form=form)

@app.route('/pacjenci_dopisz')
def pacjenci_dopisz_page():
    return render_template('pacjenci/dopisz.html')

@app.route('/pacjenci_wyszukaj')
def pacjenci_wyszukaj_page():
    pacjent = Pacjenci.query.all()
    return render_template('pacjenci/wyszukaj.html', Pacjenci=pacjent)

## RAPORTY

## SLOWNIKI

@app.route('/slowniki_oddzialy')
def slowniki_oddzialy_page():
    oddzial = Oddzialy.query.all()
    return render_template('slowniki/oddzialy.html', Oddzialy=oddzial)

@app.route('/dodaj_uzytkownika', methods=['GET', 'POST'])
def dodaj_uzytkownika_page():
    form = RegisterUserForm()
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

    return render_template('dodaj/uzytkownika.html', form=form)

@app.route('/slowniki_uzytkownicy')
def slowniki_uzytkownicy_page():
    uzytkownik = Uzytkownicy.query.all()
    return render_template('slowniki/uzytkownicy.html', Uzytkownicy=uzytkownik)

@app.route('/slowniki_wlasciciel')
def slowniki_wlasciciel_page():
    owner = Owners.query.all()
    return render_template('slowniki/owner.html', Owners=owner)

@app.route('/slowniki_wlasciciel_edytuj')
def slowniki_wlasciciel_edytuj_page():
    owner = Owners.query.all()
    return render_template('slowniki/owner-edytuj.html', Owners=owner) 

#### MODULY

@app.route('/moduly')
def modules_page():
    return render_template('modules.html')

### LOGIN

@app.route('/zaloguj')
def login_page():
    return render_template('login.html')

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