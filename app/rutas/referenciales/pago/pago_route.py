from flask import Blueprint, render_template

pagmod = Blueprint('pago', __name__, template_folder='templates')

@pagmod.route('/pago-index')
def pagoIndex():
    return render_template('pago-index.html')