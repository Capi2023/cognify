import random
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CrimeType:
    VIOLENT = "Violento"
    FINANCIAL = "Financiero"
    HATE = "Odio"
    GENERIC = "Genérico"
    CYBER = "Cibernético"
    DRUG_TRAFFICKING = "Tráfico de Drogas"
    HUMAN_TRAFFICKING = "Tráfico de Personas"
    PROPERTY = "Robo de Propiedad"
    FRAUD = "Fraude"
    ENVIRONMENTAL = "Delito Ambiental"

class Memory:
    def __init__(self, description, empathy=False, remorse=False, impact="Low"):
        self.description = description
        self.empathy = empathy
        self.remorse = remorse
        self.impact = impact

class MemoryFactory:
    @staticmethod
    def get_memories(crime_type):
        descriptions = []

        if crime_type == CrimeType.VIOLENT:
            descriptions = [
                "Experiencia desde la perspectiva de la víctima en situaciones violentas",
                "Sentimiento de impotencia ante la agresión de un ser querido",
                "Percepción de las secuelas físicas y emocionales de una agresión",
                "Vivencia de ver a alguien cercano en peligro por la violencia",
                "Conciencia de la pérdida de oportunidades debido a la violencia"
            ]
        elif crime_type == CrimeType.FINANCIAL:
            descriptions = [
                "Consecuencias económicas y sociales de los actos financieros",
                "Recuerdo de la ansiedad causada por la pérdida de dinero",
                "Impacto en familias debido a pérdidas financieras",
                "Percepción de una vida de estrés y problemas económicos",
                "Conciencia de la ruina financiera de empresas y familias"
            ]
        elif crime_type == CrimeType.HATE:
            descriptions = [
                "Comprensión y respeto por la diversidad y la igualdad",
                "Vivencia de rechazo social debido a diferencias",
                "Percepción de exclusión en una comunidad diversa",
                "Conciencia del impacto emocional del odio en otros",
                "Reflexión sobre el sufrimiento causado por prejuicios"
            ]
        elif crime_type == CrimeType.CYBER:
            descriptions = [
                "Impacto de los ciberataques en la privacidad personal",
                "Conciencia de la ansiedad causada por robos de identidad",
                "Impacto psicológico de violaciones de datos personales",
                "Recuerdo de los problemas causados por el fraude en línea",
                "Percepción de la desconfianza que genera la inseguridad digital"
            ]
        elif crime_type == CrimeType.DRUG_TRAFFICKING:
            descriptions = [
                "Sufrimiento de personas afectadas por el abuso de drogas",
                "Impacto social de la adicción y la pérdida de seres queridos",
                "Percepción de las familias destruidas por el narcotráfico",
                "Conciencia de las consecuencias para la salud pública",
                "Sentimiento de pérdida por la influencia de las drogas en la comunidad"
            ]
        elif crime_type == CrimeType.HUMAN_TRAFFICKING:
            descriptions = [
                "Empatía con las víctimas de trata de personas y esclavitud",
                "Impacto de la explotación en la vida y la dignidad humana",
                "Conciencia del trauma psicológico causado a las víctimas",
                "Percepción del sufrimiento de las familias afectadas",
                "Reflexión sobre la pérdida de derechos y libertades"
            ]
        elif crime_type == CrimeType.PROPERTY:
            descriptions = [
                "Pérdida y daño causado por la sustracción de bienes ajenos",
                "Sentimiento de invasión al perder posesiones personales",
                "Conciencia de la inseguridad generada por los robos",
                "Impacto emocional de la pérdida de pertenencias",
                "Reflexión sobre el esfuerzo necesario para reponer pérdidas"
            ]
        elif crime_type == CrimeType.FRAUD:
            descriptions = [
                "Sufrimiento de quienes perdieron dinero por fraudes",
                "Impacto de la traición financiera en la vida de las personas",
                "Conciencia del daño económico en familias y empresas",
                "Percepción de la ansiedad causada por la pérdida de ahorros",
                "Reflexión sobre la desconfianza generada por los fraudes"
            ]
        elif crime_type == CrimeType.ENVIRONMENTAL:
            descriptions = [
                "Conciencia de los daños al medio ambiente y sus efectos",
                "Percepción de la destrucción de recursos naturales",
                "Reflexión sobre el impacto en la vida silvestre y ecosistemas",
                "Empatía hacia comunidades afectadas por daños ambientales",
                "Conciencia del impacto ambiental a largo plazo"
            ]
        else:  # GENERIC
            descriptions = [
                "Reflexión sobre las consecuencias de las acciones",
                "Conciencia general sobre el impacto en la sociedad",
                "Reflexión sobre la importancia de la empatía",
                "Percepción de la necesidad de cambio personal",
                "Vivencias que invitan a la autorreflexión"
            ]

        memories = []
        for desc in descriptions:
            empathy = random.choice([True, False])
            remorse = random.choice([True, False])
            impact = random.choice(["Bajo", "Medio", "Alto"])
            memories.append(Memory(description=desc, empathy=empathy, remorse=remorse, impact=impact))

        return memories

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
