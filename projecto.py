from app import app, db
from models import Proyect


with app.app_context():
    nuevo_proyecto = Proyect(
        nombre="Mi Proyecto de Ejemplo",
        descripcion="Descripción del proyecto",
        imagen="imagen_de_ejemplo.jpg"
    )
    db.session.add(nuevo_proyecto)
    db.session.commit()
