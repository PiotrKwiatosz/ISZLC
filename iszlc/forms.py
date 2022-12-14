from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError
from iszlc.models import Uzytkownicy, Pacjenci, Recepty, Leki, Roztwory

## UZYTKOWNIK
class RegisterUzytkownicyForm(FlaskForm):
    def validate_username(self, username_to_check):
        username = Uzytkownicy.query.filter_by(username=username_to_check.data).first()
        if username:
            raise ValidationError('Użytkownik aktualnie już istnieje! Prosze sprobuj inne nazwisko użykownika')

    username = StringField(label='Nazwa użytkownia:', validators=[Length(min=1, max=30), DataRequired()])
    nazwisko = StringField(label='Nazwisko:', validators=[Length(min=4, max=60), DataRequired()])
    imie = StringField(label='Imię:', validators=[Length(min=2, max=30), DataRequired()])
    pwz = StringField(label='PWZ:')
    tytul_naukowy = StringField(label='Tytuł naukowy:')
    uprawnienia = StringField(label='Uprawnienia:')
    password1 = PasswordField(label='Hasło:', validators=[Length(min=4), DataRequired()])
    password2 = PasswordField(label='Powtórz hasło:', validators=[EqualTo('password1'), DataRequired()])
    
    submit = SubmitField(label='Dodaj!')

## LOGIN
class LoginForm(FlaskForm):
    username = StringField(label='Nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField(label='Haslo:', validators=[DataRequired()])

    submit = SubmitField(label='Zaloguj się!')

## WYSZUKIWANIE
class SearchForm(FlaskForm):
	searched = StringField("Szukane:", validators=[DataRequired()])
	submit = SubmitField("Szukaj!")



## PACJENT
class RegisterPacjenciForm(FlaskForm):
    nazwisko = StringField(label='Nazwisko:', validators=[Length(min=3, max=60), DataRequired()])
    def validate_pesel(self, nazwisko_to_check):
        nazwisko = Pacjenci.query.filter_by(nazwisko=nazwisko_to_check.data).first()
        if nazwisko:
            raise ValidationError('Podane nazwisko jest za krótkie, powinno mieć od 3 do 60 znaków! Prosze sprobuj jeszcze raz')

    pierwsze_imie = StringField(label='Imię (pierwsze):', validators=[Length(min=2, max=30), DataRequired()])
    def validate_pierwsze_imie(self, pierwsze_imie_to_check):
        pierwsze_imie = Pacjenci.query.filter_by(pierwsze_imie=pierwsze_imie_to_check.data).first()
        if pierwsze_imie:
            raise ValidationError('Podane pierwsze imię jest za krótkie! Musi mieć od 2 do 30 znaków. Prosze sprobuj jeszcze raz')

    drugie_imie = StringField(label='Drugie imię:')
    def validate_drugie_imie(self, drugie_imie_to_check):
        drugie_imie = Pacjenci.query.filter_by(drugie_imie=drugie_imie_to_check.data).first()
        if drugie_imie:
            raise ValidationError('Podane drugie imię jest za krótkie! Musi mieć od 2 do 30 znaków. Prosze sprobuj jeszcze raz')

    pesel = StringField(label='PESEL:')
    def validate_pesel(self, pesel_to_check):
        pesel = Pacjenci.query.filter_by(pesel=pesel_to_check.data).first()
        if pesel:
            raise ValidationError('Pacjent z podanym PESELem aktualnie już jest! Prosze sprobuj inny PESEL')

    data_urodzenia = StringField(label='Data urodzenia:')
    def validate_data_urodzenia(self, data_urodzenia_to_check):
        data_urodzenia = Pacjenci.query.filter_by(data_urodzenia=data_urodzenia_to_check.data).first()
        if data_urodzenia:
            raise ValidationError('Data urodzenia nie może być pusta! I ma mieć od 8 do 10 znaków. Prosze sprobuj jeszcze raz')

    badanie = StringField(label='Badanie:')

    nr_w_badaniu = StringField(label='Numer w badaniu:', validators=[Length(min=1), DataRequired()])
    def validate_nr_w_badaniu(self, nr_w_badaniu_to_check):
        nr_w_badaniu = Pacjenci.query.filter_by(nr_w_badaniu=nr_w_badaniu_to_check.data).first()
        if nr_w_badaniu:
            raise ValidationError('Podany numer aktualnie istnieje! Prosze sprobuj inny numer')
    
    submit = SubmitField(label='Dodaj!')

## RECEPTY
class RegisterReceptyForm(FlaskForm):
    def validate_nr_recepty(self, nr_recepty_to_check):
        nr_recepty = Recepty.query.filter_by(nr_recepty=nr_recepty_to_check.data).first()
        if nr_recepty:
            raise ValidationError('Recepta już istnieje! Prosze sprobuj inny numer recepty')

    nr_recepty = StringField(label='Numer recepty:', validators=[Length(min=4, max=60), DataRequired()])
    data_wypis = StringField(label='Data wypisania:', validators=[Length(min=2, max=12), DataRequired()])
    data_wyprod = StringField(label='Data wyprodukowania:', validators=[Length(min=2, max=12), DataRequired()])
    data_pod = StringField(label='Data podania:', validators=[Length(min=2, max=12), DataRequired()])
    pacjent_id = StringField(label='Numer pacjenta:', validators=[DataRequired()])
    odd_id = StringField(label='Numer oddziału:', validators=[DataRequired()])
    lek_id = StringField(label='Numer leku:', validators=[DataRequired()])
    roztwor_id = StringField(label='Numer roztworu:', validators=[DataRequired()])
    droga_pod = StringField(label='Droga podania:')
    predkosc_pod = StringField(label='Prędkość podania:')
    data_waz = StringField(label='Data ważności:', validators=[Length(min=4), DataRequired()])
    godz_waz = StringField(label='Godzina ważności:')
    zatwierdzony = StringField(label='Zatwierdzony:', validators=[Length(min=1), DataRequired()])
    
    submit = SubmitField(label='Dodaj!')

## LEKI
class RegisterLekiForm(FlaskForm):
    def validate_nazwisko(self, nazwa_miedzynarodowa_to_check):
        nazwa_miedzynarodowa = Leki.query.filter_by(nazwa_miedzynarodowa=nazwa_miedzynarodowa_to_check.data).first()
        if nazwa_miedzynarodowa:
            raise ValidationError('Lek już istnieje! Prosze sprobuj inną nazwe leku')

    def validate_pwz(self, ean_to_check):
        ean = Leki.query.filter_by(ean=ean_to_check.data).first()
        if ean:
            raise ValidationError('Podany aktualnie istnieje! Prosze sprobuj inny numer')


    nazwa_handlowa = StringField(label='Nazwa handlowa leku:', validators=[Length(min=4, max=60), DataRequired()])
    nazwa_miedzynarodowa = StringField(label='Nazwa międzynarodowa leku:', validators=[Length(min=2, max=30)])
    ean = StringField(label='EAN:', validators=[DataRequired()])
    dawka = StringField(label='Dawka:', validators=[Length(min=1)])
    producent = StringField(label='Producent:', validators=[Length(min=2)])
    subst_czynna = StringField(label='Substancja czynna:')
    
    submit = SubmitField(label='Dodaj!')

## ROZTWORY
class RegisterRoztworyForm(FlaskForm):
    def validate_nazwa_handlowa(self, nazwa_handlowa_to_check):
        nazwa_handlowa = Roztwory.query.filter_by(nazwa_handlowa=nazwa_handlowa_to_check.data).first()
        if nazwa_handlowa:
            raise ValidationError('Roztwór już istnieje! Prosze sprobuj innej nazwy')

    ean = StringField(label='EAN:', validators=[Length(min=2, max=60)])
    nazwa_handlowa = StringField(label='Nazwa handlowa:', validators=[DataRequired()])
    nazwa_miedzynarodowa = StringField(label='Nazwa międzynarodowa:', validators=[DataRequired()])
    dawka = StringField(label='Dawka:', validators=[Length(min=2, max=20), DataRequired()])
    producent = StringField(label='Producent:', validators=[Length(min=2, max=80), DataRequired()])
    subst_czynna = StringField(label='Substancja czynna:', validators=[Length(min=2, max=30), DataRequired()])
    zawartosc_subst_ml = StringField(label='Zawartość substancji w ml:', validators=[Length(min=2, max=30), DataRequired()])
    opis_op = StringField(label='Opis opakowania:', validators=[DataRequired()])
    obj_op_ml = StringField(label='Objętość opakowania w ml:', validators=[Length(min=1, max=20), DataRequired()])
    postac = StringField(label='Postać:', validators=[Length(min=2, max=30), DataRequired()])
    barwa = StringField(label='Barwa:', validators=[Length(min=2, max=10), DataRequired()])
    droga_pod = StringField(label='Data podania:', validators=[Length(min=2, max=30), DataRequired()])
    okres_waz_prod = StringField(label='Okres ważności (wg. producenta):', validators=[Length(min=2, max=30), DataRequired()])
    temp_prz_prod = StringField(label='Temperatura przygotowania (wg. producenta):', validators=[Length(min=2, max=30), DataRequired()])

    submit = SubmitField(label='Dodaj!')