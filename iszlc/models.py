from iszlc import db

class Doctors(db.Model):
    doctor_id = db.Column(db.Integer(), primary_key=True)
    doctor_name = db.Column(db.String(), nullable=False, unique=False)
    doctor_surname = db.Column(db.String(), nullable=False, unique=True)
    doctor_nr = db.Column(db.Integer(), nullable=True, unique=True)

    def __repr__(self):
        return f'Doktor {self.doctor_surname}'