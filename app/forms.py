from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class CustomizationForm(Form):
	head = SelectField('Head', choices = [('happy.png', 'Happy Face'), ('sad.png', 'Sad Face'), 'surprised.png', ('Surprised Face')])
	torso = SelectField('Body', choices = [('blackbody.png', 'Black'), ('greenbody.png', 'Green'), ('bluebody.png', 'Blue')])
	shoes = SelectField('Shoes', choices = [('blackshoes.png', 'Black'), ('greenshoes.png', 'Green'), ('blueshoes.png', 'Blue')])
	titleUpdate = StringField('Update Title')
	submit = SubmitField('Save Hero!!')
