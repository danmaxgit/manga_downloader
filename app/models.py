from app         import db, bcrypt
from flask_login import UserMixin

ROLE_USER = 0
ROLE_ADMIN = 1

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id       = db.Column(db.Integer,      primary_key = True)
    user     = db.Column(db.String(64),   unique = True)
    password = db.Column(db.String(500))
    role     = db.Column(db.SmallInteger, default = ROLE_USER)

    def __init__(self, user, password):
        self.user       = user
        self.password   = bcrypt.generate_password_hash(password).decode("utf-8")

    def __repr__(self):
        return str(self.id) + ' - ' + str(self.user)

    def save(self):

        # inject self into db session    
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self 

class Title(db.Model):
    __tablename__ = "titles"
    id           = db.Column(db.Integer,     primary_key = True)
    name         = db.Column(db.String(500), unique = True)
    type         = db.Column(db.SmallInteger)
    link         = db.Column(db.String(500), unique = True)
    last_chapter = db.Column(db.Integer)

    def __init__(self, name, type, link, last_chapter = 1):
        self.name = name
        self.type = type
        self.link = link
        self.last_chapter = last_chapter

    def __repr__(self):
        return str(self.name) + " -> " + str(srld.last_chapter)
