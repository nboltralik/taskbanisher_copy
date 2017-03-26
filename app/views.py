from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from .forms import CustomizationForm
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

    class quest_object():
        name = 'nothing'
        tasks = []
    quest_objects = []
    quests = models.Quest.query.all()
    for q in quests:
        if q.author.username == 'David':
            quest_object_instance = quest_object()
            quest_object_instance.name = q.questName
            quest_object.tasks = user.get_project(q.questName).get_tasks()
            quest_objects.append(quest_object_instance)

    return render_template('index.html',
                           title='Home',
                           user=user,
                           karma=karma,
                           tasks=tasks,
                           sample_project=sample_project,
                           quest_objects=quest_objects)
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
    project_name = models.Quest.query.get(1).questName
    project = user.get_project(project_name)
    return render_template('index.html',
                           title='Home',
                           user=user,
                           users=users)
    return render_template('quests.html')

@app.route('/customization')
def customization():
    form = CustomizationForm()
    return render_template('customization.html',
                           form=form)
