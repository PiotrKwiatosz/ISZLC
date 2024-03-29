from iszlc import app
from flask import render_template, redirect, url_for, flash
from iszlc.models import Pacjenci, Recepty, Leki, Roztwory 
from iszlc.models import Uzytkownicy, Wlasciciele, Oddzialy
from iszlc.forms import RegisterUzytkownicyForm, LoginForm, SearchForm
from iszlc.forms import RegisterPacjenciForm, RegisterReceptyForm, RegisterLekiForm, RegisterRoztworyForm
from iszlc import db
from flask_login import login_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

#### MAIN

@app.route('/iszlc', methods=['GET', 'POST'])
@login_required
def iszlc_page():
    return render_template('iszlc.html')

## LOGIN

@app.route('/dodaj_uzytkownika', methods=['GET', 'POST'])
def dodaj_uzytkownika_page():
    form = RegisterUzytkownicyForm()
    if form.validate_on_submit():
        uzytkownik_to_create = Uzytkownicy(username=form.username.data,
                                            nazwisko=form.nazwisko.data,
                                            imie=form.imie.data,
                                            pwz=form.pwz.data,
                                            tytul_naukowy=form.tytul_naukowy.data,
                                            uprawnienia=form.uprawnienia.data,
                                            password=form.password1.data)
        db.session.add(uzytkownik_to_create)
        db.session.commit()
        login_user(uzytkownik_to_create)
        flash(f"Użytkownik dodany pomyślnie! Jesteś teraz zalogowany jako {uzytkownik_to_create.username}", category='success')
        return redirect(url_for('iszlc_page'))

    if form.errors != {}: #Jesli nie ma bledow z validatora
        for err_msg in form.errors.values():
            flash(f'Bląd dodania użytkownika: {err_msg}', category='danger')

    return render_template('dodaj/uzytkownika.html', form=form)           

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_uzytkownik = Uzytkownicy.query.filter_by(username=form.username.data).first()
        if attempted_uzytkownik and attempted_uzytkownik.check_password_correction(
                attempted_password=form.password.data):
            login_user(attempted_uzytkownik)
            flash(f'Sukces! Zalogowałeś się jako: {attempted_uzytkownik.username}', category='success')
            return redirect(url_for('iszlc_page'))
        else:
            flash('Użytkownik i hasło nie pasują! Spróbuj jeszcze raz', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("Właśnie się wylogowałeś!", category='info')
    return redirect(url_for("home_page"))


## SZUKAJ

@app.context_processor
def base():
	form = SearchForm()
	return dict(form=form)

@app.route('/leki_szukaj', methods=['POST'])
def leki_szukaj():
	form = SearchForm()
	lek = Leki.query
	if form.validate_on_submit():
		# Get data from submitted form
		lek.searched = form.searched.data
		# Query the Database
		Leki = Leki.filter(Leki.nazwa_handlowa.like('%' + Leki.searched + '%'))
		Leki = Leki.order_by(Leki.nazwa_handlowa).all()

		return render_template('leki/szukaj.html', 		 
        form=form, 		 
        searched = Leki.searched,
		Leki = lek)

## LEKI

@app.route('/leki_wyszukaj')
def leki_wyszukaj_page():
    lek = Leki.query.all()
    return render_template('leki/wyszukaj.html', Leki=lek)

@app.route('/dodaj_leki', methods=['GET', 'POST'])
def dodaj_leki_page():
    form = RegisterLekiForm()
    if form.validate_on_submit():
        lek_to_create = Leki(ean=form.ean.data,
                            nazwa_handlowa=form.nazwa_handlowa.data,
                            nazwa_miedzynarodowa=form.nazwa_miedzynarodowa.data)
        db.session.add(lek_to_create)
        db.session.commit()
        flash(f"Lek dodany pomyślnie!", category='success')
        return redirect(url_for('leki_wyszukaj_page'))

    if form.errors != {}: #Jesli nie ma bledow z validatora
        for err_msg in form.errors.values():
            flash(f'Bląd dodania leku: {err_msg}', category='danger')

    return render_template('dodaj/leki.html', form=form)

## RECEPTY

@app.route('/dodaj_recepta', methods=['GET', 'POST'])
def dodaj_recepta_page():
    form = RegisterReceptyForm()
    if form.validate_on_submit():
        recepta_to_create = Recepty(nr_recepty=form.nr_recepty.data,
                                    data_wypis=form.data_wypis.data,
                                    data_wyprod=form.data_wyprod.data,
                                    data_pod=form.data_pod.data,
                                    id_pacjent=form.id_pacjent.data,
                                    id_odd=form.id_odd.data,
                                    id_lek=form.id_lek.data,
                                    id_roztow=form.id_roztwor.dodaj_recepta_page,
                                    droga_pod=form.droga_pod.data,
                                    predkosc_pod=form.predkosc_pod.data,
                                    data_waznosci=form.data_waznosci.data,
                                    godz_waznosci=form.godzina_waznosci.data,
                                    zatwierdzony=form.zatwierdzony.data)
        db.session.add(recepta_to_create)
        db.session.commit()
        flash(f"Recepta dodana pomyślnie!", category='success')
        return redirect(url_for('recepty_wyszukaj_page'))

    if form.errors != {}: #Jesli nie ma bledow z validatora
        for err_msg in form.errors.values():
            flash(f'Bląd dodania recepty: {err_msg}', category='danger')

    return render_template('dodaj/recepta.html', form=form)

@app.route('/recepty_szukaj')
def recepty_szukaj_page():
    return render_template('recepty/szukaj.html')

@app.route('/recepty_wyszukaj')
def recepty_wyszukaj_page():
    recepta = Recepty.query.all()
    return render_template('recepty/wyszukaj.html', Recepty=recepta)

@app.route('/recepty_drukuj')
def recepty_drukuj_page():
    return render_template('recepty/drukuj.html')

## PACJENCI

@app.route('/dodaj_pacjenta', methods=['GET', 'POST'])
def dodaj_pacjenta_page():
    form = RegisterPacjenciForm()
    if form.validate_on_submit():
        pacjent_to_create = Pacjenci(nazwisko=form.nazwisko.data,
                                    pierwsze_imie=form.pierwsze_imie.data,
                                    drugie_imie=form.drugie_imie.data,
                                    pesel=form.pesel.data,
                                    data_urodzenia=form.data_urodzenia.data,
                                    badanie=form.badanie.data,
                                    nr_w_badaniu=form.nr_w_badaniu.data)
        db.session.add(pacjent_to_create)
        db.session.commit()
        flash(f"Pacjent dopisany pomyślnie!", category='success')
        return redirect(url_for('iszlc_page'))

    if form.errors != {}: #Jesli nie ma bledow z validatora
        for err_msg in form.errors.values():
            flash(f'Bląd dopisywania pacjenta: {err_msg}', category='danger')

    return render_template('dodaj/pacjenta.html', form=form)

@app.route('/pacjenci_wyszukaj')
def pacjenci_wyszukaj_page():
    pacjent = Pacjenci.query.all()
    return render_template('pacjenci/wyszukaj.html', Pacjenci=pacjent)

## SLOWNIKI

@app.route('/slowniki_oddzialy')
def slowniki_oddzialy_page():
    oddzial = Oddzialy.query.all()
    return render_template('slowniki/oddzialy.html', Oddzialy=oddzial)

@app.route('/slowniki_uzytkownicy')
def slowniki_uzytkownicy_page():
    uzytkownik = Uzytkownicy.query.all()
    return render_template('slowniki/uzytkownicy.html', Uzytkownicy=uzytkownik)

@app.route('/slowniki_wlasciciel')
def slowniki_wlasciciel_page():
    wlasciciel = Wlasciciele.query.all()
    return render_template('slowniki/wlasciciel.html', Wlasciciele=wlasciciel)

@app.route('/slowniki_wlasciciel_edytuj')
def slowniki_wlasciciel_edytuj_page():
    wlasciciel = Wlasciciele.query.all()
    return render_template('slowniki/wlasciciel-edytuj.html', Wlasciciele=wlasciciel) 

#### MODULY

@app.route('/moduly')
def modules_page():
    return render_template('modules.html')