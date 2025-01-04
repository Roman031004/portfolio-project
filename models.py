from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Proyect(db.Model):
    __tablename__ = 'proyect' 

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(255))
    imagen = db.Column(db.String(255))

