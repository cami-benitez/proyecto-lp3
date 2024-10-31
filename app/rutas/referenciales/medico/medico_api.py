from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.Medico.MedicoDao import MedicoDao
medico_api = Blueprint('medico_api', __name__)

# Trae todos los médicos
@medico_api.route('/medicos', methods=['GET'])
def getMedicos():
    medico_dao = MedicoDao()

    try:
        medicos = medico_dao.getMedicos()

        return jsonify({
            'success': True,
            'data': medicos,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los médicos: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@medico_api.route('/medicos/<int:medico_id>', methods=['GET'])
def getMedico(medico_id):
    medico_dao = MedicoDao()

    try:
        medico = medico_dao.getMedicoById(medico_id)

        if medico:
            return jsonify({
                'success': True,
                'data': medico,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el médico con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener médico: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo médico
@medico_api.route('/medicos', methods=['POST'])
def addMedico():
    data = request.get_json()
    medico_dao = MedicoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'especialidad', 'dia', 'turnos']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        nombre = data['nombre'].upper()
        especialidad = data['especialidad'].upper()
        dia = data['dia'].upper()
        turnos = data['turnos']

        medico_id = medico_dao.guardarMedico(nombre, especialidad, dia, turnos)
        if medico_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': medico_id, 'nombre': nombre, 'especialidad': especialidad, 'dia': dia, 'turnos': turnos},
                'error': None
            }), 201
        else:
            return jsonify({
                'success': False,
                'error': 'No se pudo guardar el médico. Consulte con el administrador.'
            }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar médico: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@medico_api.route('/medicos/<int:medico_id>', methods=['PUT'])
def updateMedico(medico_id):
    data = request.get_json()
    medico_dao = MedicoDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['nombre', 'especialidad', 'dia', 'turnos']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    nombre = data['nombre']
    especialidad = data['especialidad']
    dia = data['dia']
    turnos = data['turnos']

    try:
        if medico_dao.updateMedico(medico_id, nombre, especialidad, dia, turnos):
            return jsonify({
                'success': True,
                'data': {'id': medico_id, 'nombre': nombre, 'especialidad': especialidad, 'dia': dia, 'turnos': turnos},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el médico con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar médico: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@medico_api.route('/medicos/<int:medico_id>', methods=['DELETE'])
def deleteMedico(medico_id):
    medico_dao = MedicoDao()

    try:
        if medico_dao.deleteMedico(medico_id):
            return jsonify({
                'success': True,
                'mensaje': f'Médico con ID {medico_id} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el médico con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar médico: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
