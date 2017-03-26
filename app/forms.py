from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class CustomizationForm(Form):
	head = SelectField('Head: ', choices = [('nochange', ''), ('happyFace.png', 'Happy Face'), ('sadFace.png', 'Sad Face'), ('surprisedFace.png', 'Surprised Face')])
	torso = SelectField('Torso: ', choices = [('nochange', ''), ('blackBody.png', 'Black'), ('greenBody.png', 'Green'), ('blueBody.png', 'Blue')])
	shoes = SelectField('Kicks: ', choices = [('nochange', ''), ('blackShoes.png', 'Black'), ('greenShoes.png', 'Green'), ('blueShoes.png', 'Blue')])
	title = StringField('Update Title')
	submit = SubmitField('Save Hero!!')

class AddQuestForm(Form):
    picture = SelectField('Icon: ', choices = [('', ''), ('sword.png', 'Sword')])
    name = StringField('Quest Name')
    submit = SubmitField('Start Quest!')
