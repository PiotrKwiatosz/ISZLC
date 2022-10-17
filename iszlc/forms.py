from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from iszlc.models import Doctors, Users, Leki, Pacjent

## LEKARZ
class RegisterForm(FlaskForm):
    def validate_nazwisko(self, nazwisko_to_check):
        nazwisko = Doctors.query.filter_by(nazwisko=nazwisko_to_check.data).first()
        if nazwisko:
            raise ValidationError('Doktor aktualnie istnieje! Prosze sprobuj inne nazwisko doktora')

    def validate_nr(self, nr_to_check):
        nr = Doctors.query.filter_by(nr=nr_to_check.data).first()
        if nr:
            raise ValidationError('Podany aktualnie istnieje! Prosze sprobuj inny numer')


    nazwisko = StringField(label='Nazwisko doktora:', validators=[Length(min=3, max=60), DataRequired()])
    imie = StringField(label='Imię doktora:', validators=[Length(min=2, max=30), DataRequired()])
    nr = StringField(label='Numer:', validators=[Length(min=4), DataRequired()])
    
    submit = SubmitField(label='Dodaj!')

## USERS
class RegisterForm(FlaskForm):
    def validate_nazwisko(self, nazwisko_to_check):
        nazwisko = Users.query.filter_by(nazwisko=nazwisko_to_check.data).first()
        if nazwisko:
            raise ValidationError('Użytkownik aktualnie istnieje! Prosze sprobuj inne nazwisko użykownika')

    def validate_pwz(self, pwz_to_check):
        pwz = Users.query.filter_by(pwz=pwz_to_check.data).first()
        if pwz:
            raise ValidationError('Podany aktualnie istnieje! Prosze sprobuj inny numer')


    nazwisko = StringField(label='Nazwisko użytkownika:', validators=[Length(min=4, max=60), DataRequired()])
    imie = StringField(label='Imię użytkownika:', validators=[Length(min=2, max=30), DataRequired()])
    pwz = StringField(label='PWZ:', validators=[Length(min=4), DataRequired()])
    tytul_naukowy = StringField(label='Tytuł naukowy:', validators=[Length(min=2), DataRequired()])
    uprawnienia = StringField(label='Uprawnienia:', validators=[Length(min=4), DataRequired()])
    haslo = StringField(label='Hasło:', validators=[Length(min=4), DataRequired()])
    
    submit = SubmitField(label='Dodaj!')