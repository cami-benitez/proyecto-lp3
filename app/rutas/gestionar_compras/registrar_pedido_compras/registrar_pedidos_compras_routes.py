from flask import Blueprint, render_template
from app.dao.referenciales.sucursal.sucursal_dao import SucursalDao
from app.dao.referenciales.empleado.empleado_dao import EmpleadoDao
from app.dao.referenciales.producto.ProductoDao import ProductoDao

pdcmod = Blueprint('pdcmod', __name__, template_folder='templates')

@pdcmod.route('/pedido-index')
def pedido_index():
    return render_template('pedido-index.html')

@pdcmod.route('/pedido-agregar')
def pedido_agregar():
    sdao = SucursalDao()
    empdao = EmpleadoDao()
    pdao = ProductoDao()
    return render_template('pedido-agregar.html'\
    , sucursales = sdao.get_sucursales()   
    , empleados = empdao.get_empleados()\
    , productos = pdao.get_productos())