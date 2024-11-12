# services.py
import random
from models import db, Criminal, MemoryModel, MemoryFactory, CrimeType

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
        
        # Definir un rango de años de sentencia, por ejemplo, entre 1 y 25 años
        sentence_years = random.randint(1, 25)
        
        # Opcional: puedes ajustar el rango según el tipo de crimen
        # Por ejemplo, crímenes violentos podrían tener sentencias más largas
        if criminal.crime_type == CrimeType.VIOLENT:
            sentence_years = random.randint(10, 30)
        elif criminal.crime_type == CrimeType.FINANCIAL:
            sentence_years = random.randint(5, 15)
        elif criminal.crime_type == CrimeType.HATE:
            sentence_years = random.randint(5, 20)
        elif criminal.crime_type == CrimeType.DRUG_TRAFFICKING:
            sentence_years = random.randint(8, 25)
        elif criminal.crime_type == CrimeType.HUMAN_TRAFFICKING:
            sentence_years = random.randint(15, 30)
        elif criminal.crime_type == CrimeType.PROPERTY:
            sentence_years = random.randint(1, 10)
        elif criminal.crime_type == CrimeType.FRAUD:
            sentence_years = random.randint(2, 12)
        elif criminal.crime_type == CrimeType.ENVIRONMENTAL:
            sentence_years = random.randint(3, 15)
        elif criminal.crime_type == CrimeType.CYBER:
            sentence_years = random.randint(2, 8)
        else:  # GENERIC
            sentence_years = random.randint(1, 5)

        criminal.sentencia = f"Asignado a una sentencia de {sentence_years} años de prisión"
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
