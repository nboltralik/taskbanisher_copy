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
    quest = models.Quest.query.get(1)
    latest_quest = user.get_project(quest.quest_id)
    tasks = latest_quest.get_tasks();
    karma = user.karma
    return render_template('index.html',
                           title='Home',
                           user=user,
                           karma=karma,
                           tasks=tasks,
                           latest_quest=latest_quest)
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
    user = todoist.login('davidmccoy@outlook.com', '1001052!')
    class quest_object():
        name = 'nothing'
        tasks = []
    quest_objects = []
    quests = models.Quest.query.all()
    for q in quests:
        if q.author.username == 'David':
            quest_object_instance = quest_object()
            quest_object_instance.name = q.questName
            print(q.quest_id)
            quest_object_instance.tasks = user.get_project(q.quest_id).get_tasks()
            quest_objects.append(quest_object_instance)
    return render_template('quests.html',
                           title='Quests',
                           user=user,
                           quest_objects=quest_objects)
    return render_template('quests.html')

@app.route('/customization')
def customization():
    form = CustomizationForm()
    return render_template('customization.html',
                           form=form)
