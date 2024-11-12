# services.py
from models import db, Criminal, MemoryModel, MemoryFactory

class CriminalService:
    @staticmethod
    def create_criminal(name, crime_type):
        criminal = Criminal(name=name, crime_type=crime_type)
        db.session.add(criminal)
        db.session.commit()

    @staticmethod
    def get_all_criminals():
        # Ordenar por id en orden descendente para que el más reciente esté primero
        return Criminal.query.order_by(Criminal.id.desc()).all()
    
    @staticmethod
    def apply_normal_sentence(criminal_id):
        criminal = Criminal.query.get(criminal_id)
        criminal.sentencia = "Asignado a una sentencia de 10 años de prisión"  # Ejemplo de sentencia
        db.session.commit()

    @staticmethod
    def apply_cognify(criminal_id):
        criminal = Criminal.query.get(criminal_id)
        # Genera un recuerdo aleatorio para el tipo de crimen del criminal
        memory = MemoryFactory.create_memory(criminal.crime_type)
        memory_model = MemoryModel(
            description=memory.description,
            empathy=memory.empathy,
            remorse=memory.remorse,
            impact=memory.impact,
            criminal_id=criminal.id
        )
        db.session.add(memory_model)
        db.session.commit()
