from flask_sqlalchemy import SQLAlchemy
from settings import app

db = SQLAlchemy(app)

class User(db.Model):
    __tablenmame__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True,nullable=False)
    password = db.Column(db.String(80), nullable=False)