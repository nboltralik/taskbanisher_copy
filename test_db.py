from app import db, models

#u = models.User(username='Nick', email='Nick@nick.com', password='kcin', title='Eternal Master of SQL-lite', ourKarma=9001)
#v = models.User(username='No one', email='null@null.com', password='0000', title='Literally No One', ourKarma=0)
#w = models.User(username='David', email='davidmccoy@outlook.com', password='1001052!', title='Our Glorious Leader', ourKarma=23000)
#
#db.session.add(u)
#db.session.add(v)
#db.session.add(w)
#db.session.commit()
users = models.User.query.all()

print('\n- - - - - - Users - - - - - -')
for u in users:
    print(u.username, u.title, u.email, u.password)


#u = models.User.query.get(3)
#q1 = models.Quest(questName='Finding Nemo', quest_id=10101, tasks=5, pic='Nemo.jpg', author=u)
#q2 = models.Quest(questName='Adventure', quest_id=55555, tasks=4, pic='Sword.jpg', author=u)
#q3 = models.Quest(questName='Programming in C', quest_id=99999, tasks=3, pic='C.jpg', author=u)
#
#db.session.add(q1)
#db.session.add(q2)
#db.session.add(q3)
#db.session.commit()

quests = models.Quest.query.all()

print('\n- - - - - - Quests - - - - - -')
for q in quests:
    print(q.questName, q.quest_id, q.author.username, q.pic)
print()