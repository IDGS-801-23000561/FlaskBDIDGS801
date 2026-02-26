from wtforms import Form
from flask_wtf import Form
from wtforms import StringField, IntegerField, PasswordField, FloatField, SelectField
from wtforms import EmailField
from wtforms import validators

class UserForm2(Form):
    id=IntegerField('id',
    [validators.number_range(min=1, max=20, message='valor no valido')])
    nombre=StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=20, message='requiere min=4 max=20')
    ])
    apellidos=StringField('apellidos',[
        validators.DataRequired(message='El apellido es requerido')
    ])
    email=EmailField('correo',[
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
    telefono=EmailField('telefono',[
        validators.DataRequired(message='El telefono es requerido'),
        validators.length(min=1, max=12, message='Escribe un numero valido')
    ])