from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from iszlc.models import Uzytkownicy, Pacjenci, Leki

## PACJENT
class RegisterForm(FlaskForm):
    def validate_nazwisko(self, nazwisko_to_check):
        nazwisko = Pacjenci.query.filter_by(nazwisko=nazwisko_to_check.data).first()
        if nazwisko:
            raise ValidationError('Pacjent aktualnie już jest! Prosze sprobuj inne nazwisko')

    def validate_nr_w_badaniu(self, nr_w_badaniu_to_check):
        nr_w_badaniu = Pacjenci.query.filter_by(nr_w_badaniu=nr_w_badaniu_to_check.data).first()
        if nr_w_badaniu:
            raise ValidationError('Podany numer aktualnie istnieje! Prosze sprobuj inny numer')


    nazwisko = StringField(label='Nazwisko:', validators=[Length(min=3, max=60), DataRequired()])
    pierwsze_imie = StringField(label='Imię (pierwsze):', validators=[Length(min=2, max=30), DataRequired()])
    drugie_imie = StringField(label='Drugie imię:', validators=[Length(min=2, max=30)])
    pesel = StringField(label='PESEL:', validators=[Length(min=11), DataRequired()])
    data_urodzenia = StringField(label='Data urodzenia:', validators=[Length(min=8, max=10)])
    badanie = StringField(label='Badanie:', validators=[DataRequired()])
    pnr_w_badaniu = StringField(label='Numer w badaniu:', validators=[Length(min=1), DataRequired()])
    
    submit = SubmitField(label='Dodaj!')

## USERS
class RegisterForm(FlaskForm):
    def validate_nazwisko(self, nazwisko_to_check):
        nazwisko = Uzytkownicy.query.filter_by(nazwisko=nazwisko_to_check.data).first()
        if nazwisko:
            raise ValidationError('Użytkownik aktualnie już istnieje! Prosze sprobuj inne nazwisko użykownika')

    def validate_pwz(self, pwz_to_check):
        pwz = Uzytkownicy.query.filter_by(pwz=pwz_to_check.data).first()
        if pwz:
            raise ValidationError('Podany aktualnie istnieje! Prosze sprobuj inny numer')


    nazwisko = StringField(label='Nazwisko użytkownika:', validators=[Length(min=4, max=60), DataRequired()])
    imie = StringField(label='Imię użytkownika:', validators=[Length(min=2, max=30), DataRequired()])
    pwz = StringField(label='PWZ:', validators=[Length(min=4), DataRequired()])
    tytul_naukowy = StringField(label='Tytuł naukowy:', validators=[Length(min=2), DataRequired()])
    uprawnienia = StringField(label='Uprawnienia:', validators=[Length(min=4), DataRequired()])
    haslo = StringField(label='Hasło:', validators=[Length(min=4), DataRequired()])
    
    submit = SubmitField(label='Dodaj!')

## LEKI

class RegisterForm(FlaskForm):
    def validate_nazwisko(self, nazwisko_to_check):
        nazwa_miedzynarodowa = Leki.query.filter_by(nazwisko=nazwisko_to_check.data).first()
        if nazwa_miedzynarodowa:
            raise ValidationError('Lek już istnieje! Prosze sprobuj inną nazwe leku')

    def validate_pwz(self, pwz_to_check):
        ean = Leki.query.filter_by(pwz=pwz_to_check.data).first()
        if ean:
            raise ValidationError('Podany aktualnie istnieje! Prosze sprobuj inny numer')


    nazwa_handlowa = StringField(label='Nazwa handlowa leku:', validators=[Length(min=4, max=60), DataRequired()])
    nazwa_miedzynarodowa = StringField(label='Nazwa międzynarodowa leku:', validators=[Length(min=2, max=30), DataRequired()])
    ean = StringField(label='EAN:', validators=[Length(min=4), DataRequired()])
    dawka = StringField(label='Dawka:', validators=[Length(min=2), DataRequired()])
    producent = StringField(label='Producent:', validators=[Length(min=4), DataRequired()])
    subst_czynna = StringField(label='Substancja czynna:', validators=[Length(min=4), DataRequired()])
    
    submit = SubmitField(label='Dodaj!')