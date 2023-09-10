from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DataRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    sectors = db.Column(db.String(255))
    agree_to_terms = db.Column(db.Boolean, default=False)

class Sector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    subsectors = db.relationship('Subsector', backref='sector', lazy=True)
    # El atributo 'subsectors' no crea una columna en la base de datos, sino que es una vista de los subsectores relacionados.

class Subsector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'), nullable=False)
    # La columna sector_id es una clave externa que relaciona cada subsector con su sector correspondiente