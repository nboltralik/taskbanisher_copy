from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(32), index=True, unique=True)
    title = db.Column(db.String(15), index=True, unique=False)
    ourKarma = db.Column(db.Integer, index=True, unique=False)
    
    head = db.Column(db.String(10), index=True, unique=False)
    body = db.Column(db.String(10), index=True, unique=False)
    feet = db.Column(db.String(10), index=True, unique=False)
    
    quests = db.relationship('Quest', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Title %r>' % (self.username)

class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questName = db.Column(db.String(64), index=True, unique=False)
    quest_id = db.Column(db.String(64), index=True, unique=False)
    tasks = db.Column(db.Integer, index=True, unique=False)
    pic = db.Column(db.String(32), index=True, unique=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Quest: %r>' % (self.questName)