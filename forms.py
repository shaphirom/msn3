from flask_wtf import FlaskForm

from wtforms import StringField, EmailField, InputField, TextAreaField
from wtforms.validators import DataRequired, Email

class UsuarioForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Contraseña", validators=[DataRequired()])
    password_validate = StringField("Contraseña", validators=[DataRequired()])


class MensajeForm(FlaskForm):
    mensaje = TextAreaField("Mensaje")