from datetime import date
from sqlite3 import Date
from utils.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    daterime = db.Column(db.datetime)

    def __init__(self, name, email, datetime):
        self.name = name
        self.email = email
        self.date = datetime
