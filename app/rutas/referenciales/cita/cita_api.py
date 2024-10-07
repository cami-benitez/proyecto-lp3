from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.cita.CitaDao import CitaDao

citapi = Blueprint('citapi', __name__)

# Trae todas las ciudades
@citapi.route('/cita', methods=['GET'])
def getCita():
    citdao = CitaDao()

    try:
        cita = citdao.getCita()

        return jsonify({
            'success': True,
            'data': cita,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las citas: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@citapi.route('/cita/<int:cita_id>', methods=['GET'])
def getCitas(cita_id):
    citdao = CitaDao()

    try:
        cita = citdao.getCitaById(cita_id)

        if cita:
            return jsonify({
                'success': True,
                'data': cita,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la cita con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener cita: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva ciudad
@citapi.route('/cita', methods=['POST'])
def addCita():
    data = request.get_json()
    citdao = CitaDao()

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
        cita_id = citdao.guardarCita(descripcion)
        if cita_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': cita_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la cita. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar cita: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@citapi.route('/cita/<int:cita_id>', methods=['PUT'])
def updateCita(cita_id):
    data = request.get_json()
    citdao = CitaDao()

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
        if citdao.updateCita(cita_id, descripcion):
            return jsonify({
                'success': True,
                'data': {'id': cita_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la cita con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar cita: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@citapi.route('/cita/<int:cita_id>', methods=['DELETE'])
def deleteCita(cita_id):
    citdao = CitaDao()

    try:
        # Usar el retorno de eliminarCiudad para determinar el éxito
        if citdao.deleteCita(cita_id):
            return jsonify({
                'success': True,
                'mensaje': f'cita con ID {cita_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la cita con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar cita: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500