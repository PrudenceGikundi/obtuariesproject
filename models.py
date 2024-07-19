<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Obituary(db.Model):
    __tablename__ = 'obituary'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    date_of_death = db.Column(db.Date, nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    submission_date = db.Column(db.DateTime, nullable=False)
=======
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Obituary(db.Model):
    __tablename__ = 'obituary'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    date_of_death = db.Column(db.Date, nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    submission_date = db.Column(db.DateTime, nullable=False)
>>>>>>> 98e48573a57e102f6aea41acb9f24953565e4edb
    slug = db.Column(db.String(100), unique=True)