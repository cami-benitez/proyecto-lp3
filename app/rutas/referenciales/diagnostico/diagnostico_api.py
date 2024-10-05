from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.diagnostico.DiagnosticoDao import DiagnosticoDao

diagapi = Blueprint('diagapi', __name__)

# Trae todas las ciudades
@diagapi.route('/diagnostico', methods=['GET'])
def getDiagnostico():
    diadao = DiagnosticoDao()

    try:
        diagnostico = diadao.getDiagnostico()

        return jsonify({
            'success': True,
            'data':diagnostico,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas el diagnostico: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@diagapi.route('/diagnostico/<int:diagnostico_id>', methods=['GET'])
def getDiagnosticos(diagnostico_id):
    diadao = DiagnosticoDao()

    try:
        diagnostico = diadao.getDiagnosticoById(diagnostico_id)

        if diagnostico:
            return jsonify({
                'success': True,
                'data':diagnostico,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el diagnostico con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener diagnostico: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva diagnostico
@diagapi.route('/diagnostico', methods=['POST'])
def addDiagnostico():
    data = request.get_json()
    diadao = DiagnosticoDao()

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
        diagnostico_id = diadao.guardarDiagnostico(descripcion)
        if diagnostico_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': diagnostico_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el diagnostico. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregardiagnostico: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@diagapi.route('/diagnostico/<int:diagnostico_id>', methods=['PUT'])
def updateDiagnostico(diagnostico_id):
    data = request.get_json()
    diadao = DiagnosticoDao()

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
        if diadao.updateDiagnostico(diagnostico_id, descripcion):
            return jsonify({
                'success': True,
                'data': {'id': diagnostico_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el diagnostico con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizardiagnostico: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@diagapi.route('/diagnostico/<int:diagnostico_id>', methods=['DELETE'])
def deleteDiagnostico(diagnostico_id):
    diadao = DiagnosticoDao()

    try:
        # Usar el retorno de eliminarCiudad para determinar el éxito
        if diadao.deleteDiagnostico(diagnostico_id):
            return jsonify({
                'success': True,
                'mensaje': f'Diagnostico con ID {diagnostico_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el diagnostico con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar diagnostico: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500