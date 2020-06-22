from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from models import User

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField("Contraseña", validators=[DataRequired(), EqualTo('password2', message = 'Las contraseñas deben coincidir')])
    password2 = PasswordField('Confirme Contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrar')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email en uso')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Ingrasar')

class AddMensaje(FlaskForm):
    mensaje =  TextAreaField('Mensaje', validators=[DataRequired()])
    submit = SubmitField("Agregar")
