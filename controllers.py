# controllers.py
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Criminal, MemoryFactory, SimulationConfig, CrimeType
from services import CriminalService
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cognify.db'
app.config['SECRET_KEY'] = 'A3jR9KpL2vX7WqZ8sB6N1yP4'
db.init_app(app)

class CriminalForm(FlaskForm):
    name = StringField('Nombre del Delincuente', validators=[DataRequired()])
    crime_type = SelectField('Tipo de Delito', choices=[
        (CrimeType.VIOLENT, 'Violento'), 
        (CrimeType.FINANCIAL, 'Financiero'), 
        (CrimeType.HATE, 'Odio'), 
        (CrimeType.GENERIC, 'Genérico')
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
    elif choice == 'cognify':
        CriminalService.apply_cognify(criminal_id)
        flash("Cognify aplicado al criminal.")
    else:
        flash("Opción inválida seleccionada.")
    return redirect(url_for('list_criminals'))

if __name__ == '__main__':
    app.run(debug=True)
