from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.Medico.MedicoDao import MedicoDao
medapi = Blueprint('medapi', __name__)

# Trae todas las ciudades
@medapi.route('/medico', methods=['GET'])
def getMedico():
    meddao =MedicoDao()

    try:
        medico = meddao.getMedico()

        return jsonify({
            'success': True,
            'data': medico,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener medico: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@medapi.route('/medico/<int:medico_id>', methods=['GET'])
def getMedicos(medico_id):
    meddao = MedicoDao()

    try:
        medico = meddao.getMedicoById(medico_id)

        if medico:
            return jsonify({
                'success': True,
                'data': medico,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró medico con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener medico: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva ciudad
@medapi.route('/medico', methods=['POST'])
def addMedico():
    data = request.get_json()
    meddao = MedicoDao()

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
        medico_id = meddao.guardarMedico(descripcion)
        if medico_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': medico_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar medico. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar medico: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@medapi.route('/medico/<int:medico_id>', methods=['PUT'])
def updateMedico(medico_id):
    data = request.get_json()
    meddao = MedicoDao()

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
        if meddao.updateMedico(medico_id, descripcion):
            return jsonify({
                'success': True,
                'data': {'id': medico_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró medico con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar medico: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@medapi.route('/medico/<int:medico_id>', methods=['DELETE'])
def deleteMedico(medico_id):
    meddao = MedicoDao()

    try:
        # Usar el retorno de eliminarCiudad para determinar el éxito
        if meddao.deleteMedico(medico_id):
            return jsonify({
                'success': True,
                'mensaje': f'Medico con ID {medico_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró medico con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar medico: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500