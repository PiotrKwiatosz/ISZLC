from iszlc import db

class Leki(db.Model):
    id_lek = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False, unique=True)
    ean = db.Column(db.String(), nullable=True)
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

class Pacjenci(db.Model):
    id_pacjent = db.Column(db.Integer(), primary_key=True, nullable=False, autoincrement=True, unique=True)
    nazwisko = db.Column(db.String(length=30), nullable=False, unique=False)
    pierwsze_imie = db.Column(db.String(length=12), nullable=False, unique=False)
    drugie_imie = db.Column(db.String(length=12), nullable=True, unique=False)
    pesel = db.Column(db.Integer(), nullable=False, unique=True)
    data_urodzenia = db.Column(db.String(), nullable=True, unique=False)
    badanie = db.Column(db.String(), nullable=False, unique=False)
    nr_w_badaniu = db.Column(db.Integer(), nullable=False, unique=True)

    def __repr__(self):
        return f'Pacjent {self.nazwisko}'

class Uzytkownicy(db.Model):
    id_uzytkownik = db.Column(db.Integer(), primary_key=True)
    nazwisko = db.Column(db.String(length=30), nullable=True, unique=False)
    imie = db.Column(db.String(length=10), nullable=True, unique=False)
    pwz = db.Column(db.Integer(), nullable=True, unique=False)
    tytul_naukowy = db.Column(db.String(), nullable=True, unique=False)
    uprawnienia = db.Column(db.String(), nullable=True, unique=False)
    haslo = db.Column(db.String(length=30), nullable=True, unique=False)

    def __repr__(self):
        return f'Uzytkownik {self.nazwisko}'

class Owners(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nazwa = db.Column(db.String(length=30), nullable=True, unique=False)

    def __repr__(self):
        return f'Właściciel {self.nazwa}'