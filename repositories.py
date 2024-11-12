# repositories.py
from models import db, Delincuente

class DelincuenteRepository:
    @staticmethod
    def obtener_todos():
        return Delincuente.query.all()

    @staticmethod
    def agregar(delincuente):
        db.session.add(delincuente)
        db.session.commit()
