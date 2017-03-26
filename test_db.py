from app import db, models

#u = models.User(username='Nick', email='Nick@nick.com', password='kcin', title='Eternal Master of SQL-lite', ourKarma=9001)
#v = models.User(username='No one', email='null@null.com', password='0000', title='Literally No One', ourKarma=0)
#db.session.add(u)
#db.session.add(v)
#db.session.commit()
users = models.User.query.all()

for u in users:
    print(u.username, u.title, u.ourKarma)