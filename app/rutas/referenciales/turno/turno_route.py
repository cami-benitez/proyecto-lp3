from flask import Blueprint, render_template

turmod = Blueprint('turno', __name__, template_folder='templates')

@turmod.route('/ciudad-index')
def turnoIndex():
    return render_template('turno-index.html')