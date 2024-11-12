# Representación Simplificada de Clases y Relaciones (UML)
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
