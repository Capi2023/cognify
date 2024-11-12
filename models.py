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
    def create_memory(crime_type):
        memories = []

        if crime_type == CrimeType.VIOLENT:
            memories = [
                Memory("Experiencia desde la perspectiva de la víctima en situaciones violentas", empathy=True, remorse=True, impact="High"),
                Memory("Sentimiento de impotencia ante la agresión de un ser querido", empathy=True, remorse=True, impact="Medium"),
                Memory("Percepción de las secuelas físicas y emocionales de una agresión", empathy=True, remorse=False, impact="Medium"),
                Memory("Vivencia de ver a alguien cercano en peligro por la violencia", empathy=True, remorse=True, impact="High"),
                Memory("Conciencia de la pérdida de oportunidades debido a la violencia", empathy=False, remorse=True, impact="Low")
            ]

        elif crime_type == CrimeType.FINANCIAL:
            memories = [
                Memory("Consecuencias económicas y sociales de los actos financieros", empathy=True, remorse=True, impact="Medium"),
                Memory("Recuerdo de la ansiedad causada por la pérdida de dinero", empathy=False, remorse=True, impact="Low"),
                Memory("Impacto en familias debido a pérdidas financieras", empathy=True, remorse=True, impact="High"),
                Memory("Percepción de una vida de estrés y problemas económicos", empathy=False, remorse=True, impact="Medium"),
                Memory("Conciencia de la ruina financiera de empresas y familias", empathy=True, remorse=False, impact="High")
            ]

        elif crime_type == CrimeType.HATE:
            memories = [
                Memory("Comprensión y respeto por la diversidad y la igualdad", empathy=True, remorse=True, impact="High"),
                Memory("Vivencia de rechazo social debido a diferencias", empathy=True, remorse=False, impact="Medium"),
                Memory("Percepción de exclusión en una comunidad diversa", empathy=True, remorse=True, impact="High"),
                Memory("Conciencia del impacto emocional del odio en otros", empathy=True, remorse=True, impact="Medium"),
                Memory("Reflexión sobre el sufrimiento causado por prejuicios", empathy=True, remorse=False, impact="High")
            ]

        elif crime_type == CrimeType.CYBER:
            memories = [
                Memory("Impacto de los ciberataques en la privacidad personal", empathy=True, remorse=True, impact="Medium"),
                Memory("Conciencia de la ansiedad causada por robos de identidad", empathy=True, remorse=True, impact="High"),
                Memory("Impacto psicológico de violaciones de datos personales", empathy=True, remorse=False, impact="High"),
                Memory("Recuerdo de los problemas causados por el fraude en línea", empathy=False, remorse=True, impact="Medium"),
                Memory("Percepción de la desconfianza que genera la inseguridad digital", empathy=True, remorse=False, impact="Medium")
            ]

        elif crime_type == CrimeType.DRUG_TRAFFICKING:
            memories = [
                Memory("Sufrimiento de personas afectadas por el abuso de drogas", empathy=True, remorse=True, impact="High"),
                Memory("Impacto social de la adicción y la pérdida de seres queridos", empathy=True, remorse=True, impact="High"),
                Memory("Percepción de las familias destruidas por el narcotráfico", empathy=True, remorse=False, impact="High"),
                Memory("Conciencia de las consecuencias para la salud pública", empathy=False, remorse=True, impact="Medium"),
                Memory("Sentimiento de pérdida por la influencia de las drogas en la comunidad", empathy=True, remorse=False, impact="Medium")
            ]

        elif crime_type == CrimeType.HUMAN_TRAFFICKING:
            memories = [
                Memory("Empatía con las víctimas de trata de personas y esclavitud", empathy=True, remorse=True, impact="High"),
                Memory("Impacto de la explotación en la vida y la dignidad humana", empathy=True, remorse=True, impact="High"),
                Memory("Conciencia del trauma psicológico causado a las víctimas", empathy=True, remorse=False, impact="High"),
                Memory("Percepción del sufrimiento de las familias afectadas", empathy=True, remorse=True, impact="Medium"),
                Memory("Reflexión sobre la pérdida de derechos y libertades", empathy=True, remorse=True, impact="Medium")
            ]

        elif crime_type == CrimeType.PROPERTY:
            memories = [
                Memory("Pérdida y daño causado por la sustracción de bienes ajenos", empathy=True, remorse=True, impact="Medium"),
                Memory("Sentimiento de invasión al perder posesiones personales", empathy=True, remorse=False, impact="Low"),
                Memory("Conciencia de la inseguridad generada por los robos", empathy=True, remorse=True, impact="Medium"),
                Memory("Impacto emocional de la pérdida de pertenencias", empathy=True, remorse=True, impact="High"),
                Memory("Reflexión sobre el esfuerzo necesario para reponer pérdidas", empathy=False, remorse=True, impact="Medium")
            ]

        elif crime_type == CrimeType.FRAUD:
            memories = [
                Memory("Sufrimiento de quienes perdieron dinero por fraudes", empathy=True, remorse=True, impact="High"),
                Memory("Impacto de la traición financiera en la vida de las personas", empathy=True, remorse=True, impact="High"),
                Memory("Conciencia del daño económico en familias y empresas", empathy=True, remorse=False, impact="Medium"),
                Memory("Percepción de la ansiedad causada por la pérdida de ahorros", empathy=True, remorse=True, impact="Medium"),
                Memory("Reflexión sobre la desconfianza generada por los fraudes", empathy=True, remorse=True, impact="Low")
            ]

        elif crime_type == CrimeType.ENVIRONMENTAL:
            memories = [
                Memory("Conciencia de los daños al medio ambiente y sus efectos", empathy=True, remorse=True, impact="High"),
                Memory("Percepción de la destrucción de recursos naturales", empathy=True, remorse=True, impact="High"),
                Memory("Reflexión sobre el impacto en la vida silvestre y ecosistemas", empathy=True, remorse=False, impact="High"),
                Memory("Empatía hacia comunidades afectadas por daños ambientales", empathy=True, remorse=True, impact="Medium"),
                Memory("Conciencia del impacto ambiental a largo plazo", empathy=False, remorse=True, impact="Medium")
            ]

        else:  # GENERIC
            memories = [
                Memory("Reflexión sobre las consecuencias de las acciones", empathy=False, remorse=False, impact="Low"),
                Memory("Conciencia general sobre el impacto en la sociedad", empathy=False, remorse=True, impact="Low"),
                Memory("Reflexión sobre la importancia de la empatía", empathy=True, remorse=False, impact="Medium"),
                Memory("Percepción de la necesidad de cambio personal", empathy=True, remorse=True, impact="Medium"),
                Memory("Vivencias que invitan a la autorreflexión", empathy=True, remorse=False, impact="Low")
            ]

        # Selecciona un recuerdo al azar de los definidos para el tipo de crimen
        return random.choice(memories)

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
