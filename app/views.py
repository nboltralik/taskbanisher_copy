from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from pytodoist import todoist

@app.route('/')
@app.route('/index')
def index():
    user = todoist.login('davidmccoy@outlook.com', '1001052!')
    projects = user.get_projects()
    return render_template('index.html',
                           title='Home',
                           user=user,
                           projects=projects)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)
