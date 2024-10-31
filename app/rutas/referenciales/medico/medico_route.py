from flask import Blueprint, render_template

medico_mod = Blueprint('medico', __name__, template_folder='templates')

@medico_mod.route('/medico-index')
def medicoIndex():
    return render_template('medico-index.html')