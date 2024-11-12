from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Criminal, MemoryFactory, SimulationConfig, CrimeType, MemoryModel
from services import CriminalService
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cognify.db'
app.config['SECRET_KEY'] = 'A3jR9KpL2vX7WqZ8sB6N1yP4'
db.init_app(app)

# Formulario para crear un nuevo criminal
class CriminalForm(FlaskForm):
    name = StringField('Nombre del Delincuente', validators=[DataRequired()])
    crime_type = SelectField('Tipo de Delito', choices=[
        (CrimeType.VIOLENT, 'Violento'), 
        (CrimeType.FINANCIAL, 'Financiero'), 
        (CrimeType.HATE, 'Odio'), 
        (CrimeType.GENERIC, 'Genérico'),
        (CrimeType.CYBER, 'Cibernético'),
        (CrimeType.DRUG_TRAFFICKING, 'Tráfico de Drogas'),
        (CrimeType.HUMAN_TRAFFICKING, 'Tráfico de Personas'),
        (CrimeType.PROPERTY, 'Robo de Propiedad'),
        (CrimeType.FRAUD, 'Fraude'),
        (CrimeType.ENVIRONMENTAL, 'Delito Ambiental')
    ], validators=[DataRequired()])
    submit = SubmitField('Procesar')

@app.route('/criminals', methods=['GET', 'POST'])
def list_criminals():
    form = CriminalForm()
    if form.validate_on_submit():
        name = form.name.data
        crime_type = form.crime_type.data
        CriminalService.create_criminal(name, crime_type)
        return redirect(url_for('list_criminals'))
    criminals = CriminalService.get_all_criminals()
    return render_template('criminals.html', criminals=criminals, form=form)

@app.route('/process_criminal/<int:criminal_id>', methods=['POST'])
def process_criminal(criminal_id):
    choice = request.form.get('choice')
    if choice == 'sentencia_normal':
        CriminalService.apply_normal_sentence(criminal_id)
        flash("Sentencia normal aplicada al criminal.")
        return redirect(url_for('list_criminals'))
    elif choice == 'cognify':
        return redirect(url_for('brain_mapping', criminal_id=criminal_id))
    else:
        flash("Opción inválida seleccionada.")
        return redirect(url_for('list_criminals'))

@app.route('/select_memory/<int:criminal_id>', methods=['GET', 'POST'])
def select_memory(criminal_id):
    criminal = Criminal.query.get_or_404(criminal_id)
    
    if request.method == 'POST':
        selected_memory_desc = request.form.get('memory')
        memory = next((m for m in MemoryFactory.get_memories(criminal.crime_type) if m.description == selected_memory_desc), None)
        
        if memory:
            memory_model = MemoryModel(
                description=memory.description,
                empathy=memory.empathy,
                remorse=memory.remorse,
                impact=memory.impact,
                criminal_id=criminal.id
            )
            db.session.add(memory_model)
            db.session.commit()
            return redirect(url_for('time_simulation', criminal_id=criminal_id))
        else:
            flash("Memoria no válida seleccionada.")
    
    memories = MemoryFactory.get_memories(criminal.crime_type)
    return render_template('select_memory.html', criminal=criminal, memories=memories)

@app.route('/brain_mapping/<int:criminal_id>', methods=['GET', 'POST'])
def brain_mapping(criminal_id):
    criminal = Criminal.query.get_or_404(criminal_id)
    if request.method == 'POST':
        # Después del mapeo cerebral, redirige a la selección de memoria
        return redirect(url_for('select_memory', criminal_id=criminal_id))
    return render_template('brain_mapping.html', criminal=criminal)

@app.route('/time_simulation/<int:criminal_id>', methods=['GET', 'POST'])
def time_simulation(criminal_id):
    criminal = Criminal.query.get_or_404(criminal_id)
    if request.method == 'POST':
        flash("Cognify aplicado al criminal.")
        return redirect(url_for('list_criminals'))
    return render_template('time_simulation.html', criminal=criminal)


if __name__ == '__main__':
    app.run(debug=True)
