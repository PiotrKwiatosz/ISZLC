from iszlc import db

class Leki(db.Model):
    id_lek = db.Column(db.Integer(), primary_key=True)
    ean = db.Column(db.Integer(), nullable=False, unique=True)
    nazwa_handlowa = db.Column(db.String(), nullable=False)
    nazwa_miedzynarodowa = db.Column(db.String(length=1024), nullable=False, unique=False)
    substancja_czynna = db.Column(db.String(), nullable=True, unique=False)
    producent = db.Column(db.String(length=30), nullable=False, unique=False)
    postac = db.Column(db.String(), nullable=False, unique=False)
    droga_podania = db.Column(db.String(), nullable=False, unique=False)
    zawartosc_substancji = db.Column(db.String(), nullable=False, unique=False)
    opakowanie = db.Column(db.String(), nullable=False, unique=False)
    objetosc_opakowania = db.Column(db.Integer(), nullable=False, unique=False)
    okres_waznosci_producent = db.Column(db.Date(), nullable=False, unique=False)
    okres_waznosci_fp = db.Column(db.Date(), nullable=False, unique=False)
    temperatura_fiolka_otwarta = db.Column(db.Integer(), nullable=False, unique=True)
    okres_waznosci_roztwor_producent = db.Column(db.Date(), nullable=True, unique=False)
    okres_trwalosci_roztworu_fp = db.Column(db.Date(), nullable=True, unique=False)
    temperatura_roztworu = db.Column(db.Integer(), nullable=True, unique=False)
    a_fizyko_chem_stezenie = db.Column(db.Integer(), nullable=True, unique=False)
    a_okres_waznosci = db.Column(db.Date(), nullable=True, unique=False)
    a_temperatura = db.Column(db.Integer(), nullable=True, unique=False)
    b_fizyko_chem_stezenie = db.Column(db.Integer(), nullable=True, unique=False)
    b_okres_waznosci = db.Column(db.Date(), nullable=True, unique=False)
    b_temperatura = db.Column(db.Integer(), nullable=True, unique=False)
    swiatlo = db.Column(db.String(), nullable=True, unique=False)

    def __repr__(self):
        return f'Leki {self.nazwa_handlowa}'

class Pacjenci(db.Model):
    id_pacjent = db.Column(db.Integer(), primary_key=True)
    nazwisko = db.Column(db.String(length=30), nullable=False, unique=False)
    pierwsze_imie = db.Column(db.String(length=12), nullable=False, unique=False)
    drugie_imie = db.Column(db.String(length=12), nullable=True, unique=False)
    pesel = db.Column(db.Integer(), nullable=False, unique=True)
    data_urodzenia = db.Column(db.Date(), nullable=True, unique=False)
    badanie = db.Column(db.String(), nullable=False, unique=False)
    nr_w_badaniu = db.Column(db.Integer(), nullable=False, unique=True)

    def __repr__(self):
        return f'Pacjent {self.nazwisko}'

class Uzytkownicy(db.Model):
    id_uzytkownik = db.Column(db.Integer(), primary_key=True)
    nazwisko = db.Column(db.String(length=30), nullable=False, unique=False)
    imie = db.Column(db.String(length=10), nullable=True, unique=False)
    pwz = db.Column(db.Integer(), nullable=True, unique=False)
    tytul_naukowy = db.Column(db.String(), nullable=True, unique=False)
    uprawnienia = db.Column(db.String(), nullable=True, unique=False)
    haslo = db.Column(db.String(length=30), nullable=True, unique=False)

    def __repr__(self):
        return f'Uzytkownik {self.id_uzytkownik}'