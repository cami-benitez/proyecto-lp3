from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.estadocivil.EstadocivilDao import EstadocivilDao

estapi = Blueprint('estaapi', __name__)

# Trae todas las ciudades
@estapi.route('/estadocivil', methods=['GET'])
def getEstadocivil():
    estdao = EstadocivilDao()

    try:
        estadocivil = estdao.getEstadocivil()

        return jsonify({
            'success': True,
            'data': estadocivil,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener el estadocivil: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@estapi.route('/estadocivil/<int:estadocivil_id>', methods=['GET'])
def getestadocivil(estadocivil_id):
    estdao = EstadocivilDao()

    try:
        estadocivil = estdao.getEstadocivilById(estadocivil_id)

        if estadocivil:
            return jsonify({
                'success': True,
                'data': estadocivil,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró estadocivil con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener estadocivil: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva ciudad
@estapi.route('/estadocivil', methods=['POST'])
def addEstadocivil():
    data = request.get_json()
    estdao = EstadocivilDao()

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
        estadocivil_id = estdao.guardarEstadocivil(descripcion)
        if estadocivil_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': estadocivil_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar estadocivil. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar estadocivil: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@estapi.route('/estadocivil/<int:estadocivil_id>', methods=['PUT'])
def updateEstadocivil(estadocivil_id):
    data = request.get_json()
    estdao = EstadocivilDao()

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
        if estdao.updateEstadocivil(estadocivil_id, descripcion):
            return jsonify({
                'success': True,
                'data': {'id': estadocivil_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró estadocivil con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar estadocivil: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@estapi.route('/estadocivil/<int:estadocivil_id>', methods=['DELETE'])
def deleteEstadocivil(estadocivil_id):
    estdao = EstadocivilDao()

    try:
        # Usar el retorno de eliminarCiudad para determinar el éxito
        if estdao.deleteEstadocivil(estadocivil_id):
            return jsonify({
                'success': True,
                'mensaje': f'Estadocivil con ID {estadocivil_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró estadocivil con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar estadocivil: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500