# Diagramas UML (MODELO, VISTA Y CONTROLADOR)
## Modelo

```markdown
+-------------------+
|     CrimeType     |  (Enumeración)
+-------------------+

+-------------------+            +-------------------+
|      Memory       |            |   MemoryFactory   |
+-------------------+            +-------------------+
| - description     |            | + get_memories()  |
| - empathy         |            +-------------------+
| - remorse         |
| - impact          |
+-------------------+
| + __init__()      |
+-------------------+

+-------------------+            +-------------------+
|     Criminal      |<>---------1|   MemoryModel     |
+-------------------+ 1        * +-------------------+
| - id              |            | - id              |
| - name            |            | - description     |
| - crime_type      |            | - empathy         |
| - sentencia       |            | - remorse         |
|                   |            | - impact          |
+-------------------+            | - criminal_id     |
                                +-------------------+

+-------------------+
| SimulationConfig  | (Singleton)
+-------------------+
| - settings        |
+-------------------+
| + set_setting()   |
| + get_setting()   |
+-------------------+
```
En el Modelo, las clases principales son CrimeType, Memory, MemoryFactory, Criminal, MemoryModel y SimulationConfig. CrimeType es una enumeración que define los tipos de delitos. Memory representa recuerdos con atributos como descripción, empatía y remordimiento. MemoryFactory genera listas de recuerdos basados en el tipo de delito. Criminal es un modelo de base de datos que tiene una relación uno a muchos con MemoryModel, indicando que un criminal puede tener múltiples recuerdos asociados. SimulationConfig es un singleton que gestiona la configuración de la simulación.

## Vista

```markdown
+-------------------+
|       Vista       |
+-------------------+
| + mostrar_menu_principal()    |
| + seleccionar_tipo_delito()   |
| + mostrar_recuerdo(recuerdo)  |
+-------------------+
```
La clase Vista es responsable de la interacción con el usuario. Contiene métodos estáticos como mostrar_menu_principal, seleccionar_tipo_delito y mostrar_recuerdo. Estos métodos presentan opciones al usuario y muestran información relevante. La Vista no tiene relaciones directas con otras clases en el diagrama simplificado, ya que su función es servir de interfaz entre el usuario y el sistema, mostrando datos y capturando entradas.

## Controlador

```markdown
+-------------------+          +-------------------+
|  CriminalForm     |          |  CriminalService  |
+-------------------+          +-------------------+
| - name            |          | + create_criminal()|
| - crime_type      |          | + apply_normal_sentence()|
| - submit          |          | + get_all_criminals()|
+-------------------+          +-------------------+

Flask Routes:
- /criminals -> list_criminals()
- /process_criminal/<id> -> process_criminal()
- /select_memory/<id> -> select_memory()
```
En los Controladores, destacan las rutas de Flask y la clase CriminalForm. Las rutas incluyen funciones como list_criminals, process_criminal y select_memory, que manejan solicitudes HTTP y coordinan la lógica de la aplicación. CriminalForm es un formulario que permite crear nuevos criminales con campos como nombre y tipo de delito. Los controladores interactúan con el Modelo a través de servicios como CriminalService, facilitando la comunicación entre la Vista y el Modelo y gestionando el flujo de datos y operaciones de negocio.

# Análisis del Impacto Social y Técnico del Sistema

---

## Impacto Social

### Rehabilitación Efectiva de Delincuentes

El sistema "Cognify" tiene el potencial de transformar el proceso de rehabilitación al inducir sentimientos de empatía y remordimiento en los delincuentes. Al exponer a los individuos a recuerdos que reflejan las consecuencias de sus acciones, se promueve una comprensión más profunda del impacto de sus delitos en las víctimas y la sociedad. Esta aproximación puede contribuir significativamente a reducir las tasas de reincidencia y facilitar la reintegración exitosa de los delincuentes en la comunidad.

### Conciencia y Educación Social

Además de su función rehabilitadora, Cognify puede servir como una herramienta educativa que aumente la conciencia pública sobre las repercusiones de diversos delitos. Al destacar los efectos negativos de las acciones delictivas, el sistema puede influir positivamente en la prevención del crimen y fomentar una cultura de responsabilidad y respeto hacia los demás.

### Consideraciones Éticas y Derechos Humanos

La implementación de tecnología que afecta directamente la cognición humana plantea importantes cuestiones éticas. Es fundamental garantizar que el sistema respete la autonomía y los derechos individuales de los delincuentes. Cualquier intervención debe llevarse a cabo con el consentimiento informado de los involucrados, y es imprescindible establecer límites claros para evitar posibles abusos o manipulaciones indebidas.

### Aceptación y Confianza Pública

La percepción social del uso de tecnología para influir en la mente de los individuos puede variar ampliamente. Es esencial promover la transparencia en el funcionamiento del sistema y fomentar el diálogo público para abordar preocupaciones y construir confianza. El desarrollo de políticas y regulaciones adecuadas será crucial para garantizar la legitimidad y aceptación de "Cognify" en la sociedad.

---

## Impacto Técnico

### Innovación Tecnológica y Desarrollo Modular

Cognify emplea tecnologías modernas como Flask y SQLAlchemy, y sigue el patrón de diseño Modelo-Vista-Controlador (MVC), lo que facilita su mantenimiento y escalabilidad. La arquitectura modular del sistema permite incorporar nuevos tipos de delitos y recuerdos de manera eficiente, adaptándose a las necesidades cambiantes y facilitando futuras expansiones.

### Seguridad y Protección de Datos

El manejo de información sensible requiere la implementación de medidas de seguridad robustas. Es imperativo asegurar la confidencialidad, integridad y disponibilidad de los datos personales de los delincuentes y de los recuerdos asignados. Esto incluye el uso de técnicas de cifrado, autenticación sólida y cumplimiento con regulaciones de protección de datos, como el GDPR o leyes locales aplicables.

### Integración y Compatibilidad con Sistemas Existentes

Para maximizar su eficacia, Cognify debe ser compatible e integrarse adecuadamente con los sistemas penitenciarios y de gestión existentes. Esto puede implicar desafíos técnicos relacionados con la interoperabilidad, la migración de datos y la adopción de estándares comunes. Una integración exitosa permitirá una implementación más fluida y una adopción más amplia del sistema.

### Escalabilidad y Rendimiento

A medida que el sistema se expanda y sea adoptado por más instituciones, deberá manejar un aumento en la cantidad de usuarios y volumen de datos sin comprometer el rendimiento. Es necesario diseñar la infraestructura técnica para ser escalable, utilizando prácticas de programación eficientes y posiblemente adoptando soluciones en la nube o tecnologías de microservicios.

### Desarrollo de Algoritmos Avanzados

La asignación efectiva de recuerdos personalizados a cada delincuente requiere el desarrollo de algoritmos sofisticados que puedan considerar múltiples factores, como el tipo de delito, el perfil psicológico y el historial individual. La incorporación de inteligencia artificial y aprendizaje automático puede mejorar la precisión y eficacia del sistema, aunque también agrega complejidad técnica y requiere consideraciones adicionales en cuanto a ética y transparencia algorítmica.














```markdown
# Cognify

Cognify es una aplicación basada en Flask diseñada para simular un sistema de rehabilitación criminal utilizando métodos avanzados de empatía y arrepentimiento, aplicando patrones de diseño.

## Características

- Procesamiento de criminales con opciones de "Sentencia Normal" o el programa de rehabilitación `Cognify`.
- Generación y asignación de recuerdos simulados para fomentar empatía y conciencia.
- Diseño modular siguiendo el patrón MVC con Flask y SQLAlchemy.

## Prerrequisitos

- Python 3.x
- Git
- (Opcional) Entorno virtual para Python

## Instalación

### 1. Clonar el repositorio

Clona el repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/cognify.git
cd cognify
```

### 2. Crear un entorno virtual

Es recomendable crear un entorno virtual para el proyecto. Puedes hacerlo ejecutando:

```bash
python -m venv venv
```

Activa el entorno virtual:

- En **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- En **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 3. Instalar dependencias

Instala las dependencias necesarias con `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Si utilizas Flask-Migrate, inicializa la base de datos y aplica migraciones:

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

Si no utilizas migraciones, puedes crear las tablas de la base de datos ejecutando un shell de Python:

```python
from app import db
db.create_all()
```

### 5. Configurar variables de entorno

Crea un archivo `.env` o `config.py` con las configuraciones necesarias para tu aplicación, como `SECRET_KEY` y la URI de la base de datos:

```
# .env
SECRET_KEY='your_secret_key'
SQLALCHEMY_DATABASE_URI='sqlite:///cognify.db'
```

### 6. Ejecutar la aplicación

Para iniciar el servidor de desarrollo de Flask, ejecuta:

```bash
flask run
```

La aplicación estará disponible en `http://127.0.0.1:5000`.

## Uso

1. Accede a la página principal en `http://127.0.0.1:5000/criminals`.
2. Crea un nuevo criminal seleccionando el nombre y tipo de delito.
3. Elige entre "Sentencia Normal" o `Cognify` para ver los detalles del procesamiento.

## Estructura del Proyecto

- `app.py`: Punto de entrada principal de la aplicación.
- `models.py`: Modelos de la base de datos para criminales y recuerdos.
- `controllers.py`: Controladores que manejan las rutas de la aplicación.
- `services.py`: Servicios que contienen la lógica de negocio.
- `templates/`: Plantillas HTML para la interfaz de usuario.
