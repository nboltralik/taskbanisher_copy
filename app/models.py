from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(32), index=True, unique=True)
    title = db.Column(db.String(15), index=True, unique=False)
    ourKarma = db.Column(db.Integer, index=True, unique=False)

    def __repr__(self):
        return '<Title %r>' % (self.title)

class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questName = db.Column(db.String(64), index=True, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    quest_id = db.Column(db.Integer, index=True, unique=True)

    def __repr__(self):
        return '<Quest: %r>' % (self.questName)