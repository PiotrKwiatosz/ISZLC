from iszlc import db, login_manager
from iszlc import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id_uzytkownik):
    return Uzytkownicy.query.get(int(id_uzytkownik))

class Uzytkownicy(db.Model, UserMixin):
    id_uzytkownik = db.Column(db.Integer(), primary_key=True)
    nazwisko = db.Column(db.String(length=60), nullable=True, unique=False)
    imie = db.Column(db.String(length=30), nullable=True, unique=False)
    pwz = db.Column(db.Integer(), nullable=True, unique=False)
    tytul_naukowy = db.Column(db.String(), nullable=True, unique=False)
    uprawnienia = db.Column(db.String(), nullable=True, unique=False)
    password_hash = db.Column(db.String(length=30), nullable=False)
    def get_id(self):
           return (self.id_uzytkownik)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
##

class Pacjenci(db.Model):
    id_pacjent = db.Column(db.Integer(), primary_key=True, nullable=False, autoincrement=True, unique=True)
    nazwisko = db.Column(db.String(length=60), nullable=False, unique=False)
    pierwsze_imie = db.Column(db.String(length=30), nullable=False, unique=False)
    drugie_imie = db.Column(db.String(length=30), nullable=True, unique=False)
    pesel = db.Column(db.Integer(), nullable=False, unique=True)
    data_urodzenia = db.Column(db.String(length=10), nullable=True, unique=False)
    badanie = db.Column(db.String(), nullable=True, unique=False)
    nr_w_badaniu = db.Column(db.Integer(), nullable=True, unique=True)

    def __repr__(self):
        return f'Pacjent {self.nazwisko}'

class Leki(db.Model):
    id_lek = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False, unique=True)
    ean = db.Column(db.String(length=4), nullable=True, unique=True)
    nazwa_handlowa = db.Column(db.String(), nullable=True)
    nazwa_miedzynarodowa = db.Column(db.String(), nullable=True, unique=False)
    dawka = db.Column(db.String(), nullable=True, unique=False)
    producent = db.Column(db.String(), nullable=True, unique=False)
    subst_czynna = db.Column(db.String(), nullable=True, unique=False)
    zawartosc_subst_ml = db.Column(db.String(), nullable=True, unique=False)
    zawartosc_subst_mg = db.Column(db.String(), nullable=True, unique=False)
    opis_op = db.Column(db.String(), nullable=True, unique=False)
    obj_op_ml = db.Column(db.String(), nullable=True, unique=False)
    postac = db.Column(db.String(), nullable=True, unique=False)
    barwa = db.Column(db.String(), nullable=True, unique=False)
    droga_podania = db.Column(db.String(), nullable=True, unique=False)
    okres_waz_roz_rozt_prod = db.Column(db.String(), nullable=True, unique=False)
    temp_prz_rozc_rozt_prod = db.Column(db.String(), nullable=True, unique=False)

    def __repr__(self):
        return f'Lek {self.nazwa_handlowa}'

class Owners(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nazwa = db.Column(db.String(length=30), nullable=True, unique=False)
    jednostka = db.Column(db.String(length=30), nullable=True, unique=False)
    ulica = db.Column(db.String(length=30), nullable=True, unique=False)
    miasto = db.Column(db.String(length=30), nullable=True, unique=False)

    def __repr__(self):
        return f'Właściciel {self.nazwa}'

class Oddzialy(db.Model):
    id_odd = db.Column(db.Integer(), primary_key=True)
    nazwa_odd = db.Column(db.String(length=30), nullable=True, unique=False)

    def __repr__(self):
        return f'Oddział {self.nazwa}'