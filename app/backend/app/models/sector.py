from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
