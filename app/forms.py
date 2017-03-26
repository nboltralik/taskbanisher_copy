from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class CustomizationForm(Form):
	head = SelectField('Head: ', choices = [('Happy Face'), ('Sad Face'), ('Surprised Face')])
	torso = SelectField('Body: ', choices = [('Black'), ('Green'), ('Blue')])
	shoes = SelectField('Shoes: ', choices = [('Black'), ('Green'), ('Blue')])
	titleUpdate = StringField('Update Title')
	submit = SubmitField('Save Hero!!')
