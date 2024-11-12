from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CrimeType:
    VIOLENT = "Violento"
    FINANCIAL = "Financiero"
    HATE = "Odio"
    GENERIC = "Genérico"

class Memory:
    def __init__(self, description, empathy=False, remorse=False, impact="Low"):
        self.description = description
        self.empathy = empathy
        self.remorse = remorse
        self.impact = impact

class MemoryFactory:
    @staticmethod
    def create_memory(crime_type):
        if crime_type == CrimeType.VIOLENT:
            return Memory(description="Experiencia desde la perspectiva de la víctima", empathy=True, remorse=True, impact="High")
        elif crime_type == CrimeType.FINANCIAL:
            return Memory(description="Consecuencias económicas y sociales de los actos", empathy=True, remorse=True, impact="Medium")
        elif crime_type == CrimeType.HATE:
            return Memory(description="Comprensión y respeto por la diversidad", empathy=True, remorse=True, impact="High")
        else:
            return Memory(description="Recuerdo genérico", empathy=False, remorse=False, impact="Low")

class Criminal(db.Model):
    __tablename__ = 'criminals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    crime_type = db.Column(db.String(50), nullable=False)
    sentencia = db.Column(db.String(255), nullable=True)  # Para almacenar la sentencia normal
    cognify_data = db.relationship('MemoryModel', backref='criminal', lazy=True)  # Relación con recuerdos

class MemoryModel(db.Model):
    __tablename__ = 'memories'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    empathy = db.Column(db.Boolean, default=False)
    remorse = db.Column(db.Boolean, default=False)
    impact = db.Column(db.String(50))
    criminal_id = db.Column(db.Integer, db.ForeignKey('criminals.id'), nullable=False)

class SimulationConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SimulationConfig, cls).__new__(cls)
            cls._instance.settings = {}
        return cls._instance

    def set_setting(self, key, value):
        self.settings[key] = value

    def get_setting(self, key):
        return self.settings.get(key, None)
