from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.pago.PagoDao import PagoDao

pagapi = Blueprint('pagapi', __name__)

# Trae todas las ciudades
@pagapi.route('/pago', methods=['GET'])
def getPago():
    pagdao = PagoDao()

    try:
        pago = pagdao.getPago()

        return jsonify({
            'success': True,
            'data': pago,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener los metodo: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@pagapi.route('/pago/<int:pago_id>', methods=['GET'])
def getPagos(pago_id):
    pagdao = PagoDao()

    try:
        pago = pagdao.getPagoById(pago_id)

        if pago:
            return jsonify({
                'success': True,
                'data':pago,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el metodo con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener pago: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva ciudad
@pagapi.route('/pago', methods=['POST'])
def addPago():
    data = request.get_json()
    pagdao = PagoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400

    try:
        descripcion = data['descripcion'].upper()
        pago_id = pagdao.guardarPago(descripcion)
        if pago_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': pago_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar pago. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar pago: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@pagapi.route('/pago/<int:pago_id>', methods=['PUT'])
def updatePago(pago_id):
    data = request.get_json()
    pagdao = PagoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['descripcion']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                            'success': False,
                            'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                            }), 400
    descripcion = data['descripcion']
    try:
        if pagdao.updatePago(pago_id, descripcion):
            return jsonify({
                'success': True,
                'data': {'id': pago_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró pago con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar pago: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@pagapi.route('/pago/<int:pago_id>', methods=['DELETE'])
def deletePago(pago_id):
    pagdao = PagoDao()

    try:
        # Usar el retorno de eliminarCiudad para determinar el éxito
        if pagdao.deletePago(pago_id):
            return jsonify({
                'success': True,
                'mensaje': f'metodo con ID {pago_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró pago con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar pago: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500