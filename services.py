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
        return Criminal.query.all()
    
    @staticmethod
    def apply_normal_sentence(criminal_id):
        criminal = Criminal.query.get(criminal_id)
        criminal.sentencia = "Asignado a una sentencia de 10 años de prisión"  # Mensaje de sentencia
        db.session.commit()
    
    @staticmethod
    def apply_cognify(criminal_id):
        criminal = Criminal.query.get(criminal_id)
        
        # Crear recuerdos basados en el tipo de crimen
        memories = [MemoryFactory.create_memory(criminal.crime_type)]
        for mem in memories:
            memory = MemoryModel(
                description=mem.description,
                empathy=mem.empathy,
                remorse=mem.remorse,
                impact=mem.impact,
                criminal_id=criminal.id
            )
            db.session.add(memory)
        db.session.commit()
