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
    sample_project = user.get_project('ECE 383')
    tasks = sample_project.get_tasks();
    karma = user.karma
    return render_template('index.html',
                           title='Home',
                           user=user,
                           karma=karma,
                           tasks=tasks,
                           sample_project=sample_project)
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
    #pull username and password from table
    users = models.User.query.all()
    user = todoist.login('davidmccoy@outlook.com', '1001052!')
    #define quest_object
        #objects have a quest_name and array of task_name
    #quest_objects = initialize list of quest_object
    #for q in quests:
        #create quest_object
       # if q.author.username == 'David'
       #     quest_object.quest_name = q.questName
            #create task array
          #  project = user.get_project(q.quest_name)
          #  quest_object.tasks = project.get_tasks()
    return render_template('index.html',
                           title='Home',
                           user=user,
                           users=users)
    return render_template('quests.html')

@app.route('/customization')
def customization():
    return render_template('customization.html')
