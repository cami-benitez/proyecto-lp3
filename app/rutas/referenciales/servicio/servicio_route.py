from flask import Blueprint, render_template

sermod = Blueprint('servicio', __name__, template_folder='templates')

@sermod.route('/servicio-index')
def servicioIndex():
    return render_template('servicio-index.html')