from iszlc import db, login_manager
from iszlc import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id_uzytkownik):
    return Uzytkownicy.query.get(id_uzytkownik)

class Uzytkownicy(db.Model, UserMixin):
    id_uzytkownik = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    nazwisko = db.Column(db.String(60))
    imie = db.Column(db.String(30))
    pwz = db.Column(db.Integer)
    tytul_naukowy = db.Column(db.String)
    uprawnienia = db.Column(db.String)
    password_hash = db.Column(db.String(60), nullable=False)
    
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
    id_pacjent = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    nazwisko = db.Column(db.String(60), nullable=False)
    pierwsze_imie = db.Column(db.String(30), nullable=False)
    drugie_imie = db.Column(db.String(30))
    pesel = db.Column(db.Integer, unique=True)
    data_urodzenia = db.Column(db.String(10))
    badanie = db.Column(db.String)
    nr_w_badaniu = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return f'Pacjent {self.nazwisko}'

class Recepty(db.Model):
    id_recepta = db.Column(db.Integer(), primary_key=True, nullable=False, autoincrement=True, unique=True)
    nr_recepty = db.Column(db.Integer(), nullable=False, unique=True)
    data_wypis = db.Column(db.String(), nullable=True, unique=False)
    data_wyprod = db.Column(db.String(), nullable=True, unique=False)
    data_pod = db.Column(db.String(), nullable=True, unique=False)
    id_pacjent = db.Column(db.String(), db.ForeignKey('Pacjenci.id_pacjent'))
    id_odd = db.Column(db.String(), db.ForeignKey('Oddzialy.id_odd'))
    id_lek = db.Column(db.String(), db.ForeignKey('Leki.id_lek'))
    id_roztwor = db.Column(db.String(), db.ForeignKey('Roztwory.id_roztwor'))
    droga_pod = db.Column(db.String(), nullable=True, unique=False)
    predkosc_pod = db.Column(db.String(), nullable=True, unique=False)
    data_waz = db.Column(db.String(), nullable=True, unique=False)
    godz_waz = db.Column(db.String(), nullable=True, unique=False)
    zatwierdzony = db.Column(db.String(), nullable=True, unique=False)
    
    def __repr__(self):
        return f'Recepta {self.nr_recepty}'

class Leki(db.Model):
    id_lek = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False, unique=True)
    ean = db.Column(db.String(length=4), nullable=True, unique=True)
    nazwa_handlowa = db.Column(db.String(), nullable=True, unique=False)
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

class Roztwory(db.Model):
    id_roztwor = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False, unique=True)
    ean = db.Column(db.String(length=4), nullable=True, unique=True)
    nazwa_handlowa = db.Column(db.String(), nullable=True)
    nazwa_miedzynarodowa = db.Column(db.String(), nullable=True, unique=False)
    dawka = db.Column(db.String(), nullable=True, unique=False)
    producent = db.Column(db.String(), nullable=True, unique=False)
    subst_czynna = db.Column(db.String(), nullable=True, unique=False)
    zawartosc_subst_ml = db.Column(db.String(), nullable=True, unique=False)
    opis_op = db.Column(db.String(), nullable=True, unique=False)
    obj_op_ml = db.Column(db.String(), nullable=True, unique=False)
    postac = db.Column(db.String(), nullable=True, unique=False)
    barwa = db.Column(db.String(), nullable=True, unique=False)
    droga_pod = db.Column(db.String(), nullable=True, unique=False)
    okres_waz_prod = db.Column(db.String(), nullable=True, unique=False)
    temp_prz_prod = db.Column(db.String(), nullable=True, unique=False)

    def __repr__(self):
        return f'Roztwory {self.nazwa_handlowa}'
        
class Wlasciciele(db.Model):
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