from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from .forms import CustomizationForm
from .forms import AddQuestForm
from pytodoist import todoist
from app import db, models
from sqlalchemy import func
import math

@app.route('/')
@app.route('/index')
def index():
    users = models.User.query.all()
    user = todoist.login('davidmccoy@outlook.com', '1001052!')
    quest = models.Quest.query.get(1)
    latest_quest = user.get_project(quest.quest_id)
    tasks = latest_quest.get_tasks()
    karma = user.karma
    #completed_tasks_count = len(user.get_completed_tasks())
    stats = user.get_productivity_stats()
    completed_tasks_count = stats['completed_count']
    score = (karma * .1 + completed_tasks_count * .9) * .5
    level = math.floor(score / 150)
    head = models.User.query.get(3).head
    head_path = '/static/img/' + head
    body = models.User.query.get(3).body
    body_path = '/static/img/' + body
    shoes = models.User.query.get(3).feet
    shoes_path = '/static/img/' + shoes
    hero_title = models.User.query.get(3).title
    return render_template('index.html',
                           title='Home',
                           user=user,
                           karma=score,
                           tasks=tasks,
                           latest_quest=latest_quest,
                           head_path=head_path,
                           body_path=body_path,
                           shoes_path=shoes_path,
                           hero_title=hero_title,
                           level=level)
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

@app.route('/customization', methods=['GET', 'POST'])
def customization():
    form = CustomizationForm()
    if form.validate_on_submit():
        user = models.User.query.get(3)
        if form.head.data != 'nochange':
            user.head = form.head.data
        if form.torso.data != 'nochange':
            user.body = form.torso.data
        if form.shoes.data != 'nochange':
            user.feet = form.shoes.data
        if form.title.data != '':
            user.title = form.title.data
        db.session.commit()
        return redirect('/index')
    return render_template('customization.html',
                           form=form)

@app.route('/quests/add', methods=['GET', 'POST'])
def add_quest():
    form = AddQuestForm()
    if form.validate_on_submit():
        user = models.User.query.get(3)
        if form.name.data != '':
            project_name = form.name.data
            if form.picture.data != '':
                picture = form.picture.data
            else:
                picture = 'generic.png'
            user = todoist.login('davidmccoy@outlook.com', '1001052!')
            user.add_project(project_name)
            u = models.User.query.get(3)
            quest = models.Quest(questName=project_name, quest_id=project_name, author=u)
            db.session.add(quest)
            db.session.commit()
        return redirect('/quests')
    return render_template('add_quest.html',
                           form=form)
