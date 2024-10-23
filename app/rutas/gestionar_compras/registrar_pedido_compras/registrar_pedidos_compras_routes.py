from flask import Blueprint, render_template

pdcmod = Blueprint('pdcmod', __name__, template_folder='templates')

@pdcmod.route('/pedido-index')
def pedido_index():
    return render_template('pedido-index.html')

@pdcmod.route('/pedido-agregar')
def pedido_agregar():
    return render_template('pedido-agregar.html')