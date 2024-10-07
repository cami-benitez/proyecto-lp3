from flask import Blueprint, render_template

citmod = Blueprint('cita', __name__, template_folder='templates')

@citmod.route('/cita-index')
def citaIndex():
    return render_template('cita-index.html')