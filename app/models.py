from app import db
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask import url_for

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(128), unique = True)
    password = db.Column(db.String(128), nullable = False)
    created_on = db.Column(db.DateTime(), nullable = False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)
        self.created_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "created_on": self.created_on
        }

    def __repr__(self):
        return "<User %r>" % self.username

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(128), unique = True)
    body = db.Column(db.Text)
    photo = db.Column(db.String(255))
    user_id = db.Column(db.Integer(), nullable = False)
    created_on = db.Column(db.DateTime(), nullable = False)
    updated_on = db.Column(db.DateTime(), nullable = False)

    def __init__(self, title, body, photo, user_id):
        self.title = title
        self.body = body
        self.photo = photo
        self.user_id = user_id
        self.created_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "user_id": self.user_id,
            "photo": url_for('getImage', filename=self.photo),
            "created_on": self.created_on,
            "updated_on": self.updated_on
        }

    def __repr__(self):
        return "<Article %r>" % self.title