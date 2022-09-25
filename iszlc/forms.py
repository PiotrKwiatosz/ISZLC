from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, ValidationError
from iszlc.models import Doctors


class RegisterForm(FlaskForm):
    def validate_doctor_surname(self, doctor_surname_to_check):
        doctor_surname = Doctors.query.filter_by(doctor_surname=doctor_surname_to_check.data).first()
        if doctor_surname:
            raise ValidationError('Doktor aktualnie istnieje! Prosze sprobuj inne nazwisko doktora')

    def validate_doctor_nr(self, doctor_nr_to_check):
        doctor_nr = Doctors.query.filter_by(doctor_nr=doctor_nr_to_check.data).first()
        if doctor_nr:
            raise ValidationError('Podany aktualnie istnieje! Prosze sprobuj inny numer')


    doctor_surname = StringField(label='Nazwisko doktora:', validators=[Length(min=2, max=30), DataRequired()])
    doctor_name = StringField(label='Imię doktora:', validators=[Length(min=4, max=60), DataRequired()])
    doctor_nr = StringField(label='Numer:', validators=[Length(min=4), DataRequired()])
    
    submit = SubmitField(label='Dodaj!')