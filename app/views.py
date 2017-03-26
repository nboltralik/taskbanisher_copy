from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from pytodoist import todoist
from app import db, models

@app.route('/')
@app.route('/index')
def index():
    #pull username and password from table
    users = models.User.query.all()
    user = todoist.login('davidmccoy@outlook.com', '1001052!')
    projects = user.get_projects()
    karma = user.karma
    return render_template('index.html',
                           title='Home',
                           user=user,
                           projects=projects,
                           karma=karma,
                           users=users)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user="%s", remember_me=%s' %
              (form.username.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)
@app.route('/quests')
def quests():
    return render_template('quests.html')

@app.route('/customization')
def customization():
    return render_template('customization.html')
