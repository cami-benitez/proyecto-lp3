
from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.paciente.PacienteDao import PacienteDao

pacienteapi = Blueprint('pacienteapi', __name__)

# Trae todos los pacientes
@pacienteapi.route('/pacientes', methods=['GET'])
def getPacientes():
    pacientedao = PacienteDao()

    try:
        pacientes = pacientedao.getPacientes()

        return jsonify({
            'success': True,
            'data': pacientes,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todos los pacientes: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@pacienteapi.route('/pacientes/<int:paciente_id>', methods=['GET'])
def getPaciente(paciente_id):
    pacientedao = PacienteDao()

    try:
        paciente = pacientedao.getPacienteById(paciente_id)

        if paciente:
            return jsonify({
                'success': True,
                'data': paciente,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el paciente con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener el paciente: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega un nuevo paciente
@pacienteapi.route('/pacientes', methods=['POST'])
def addPaciente():
    data = request.get_json()
    pacientedao = PacienteDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['idpe', 'edad', 'peso', 'altura']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        idpe = int(data['idpe'])
        edad = int(data['edad'])
        peso = float(data['peso'])
        altura = float(data['altura'])

        paciente_id = pacientedao.guardarPaciente(idpe, edad, peso, altura)
        if paciente_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': paciente_id, 'id_persona': idpe, 'edad': edad, 'peso': peso, 'altura': altura},
                'error': None
            }), 201
        else:
            return jsonify({'success': False, 'error': 'No se pudo guardar el paciente. Consulte con el administrador.'}), 500
    except Exception as e:
        app.logger.error(f"Error al agregar paciente: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@pacienteapi.route('/pacientes/<int:paciente_id>', methods=['PUT'])
def updatePaciente(paciente_id):
    data = request.get_json()
    pacientedao = PacienteDao()

    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['idpe', 'edad', 'peso', 'altura']

    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None or len(data[campo].strip()) == 0:
            return jsonify({
                'success': False,
                'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
            }), 400

    try:
        idpe = int(data['idpe'])
        edad = int(data['edad'])
        peso = float(data['peso'])
        altura = float(data['altura'])

        if pacientedao.updatePaciente(paciente_id, idpe, edad, peso, altura):
            return jsonify({
                'success': True,
                'data': {'id': paciente_id, 'id_persona': idpe, 'edad': edad, 'peso': peso, 'altura': altura},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el paciente con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar paciente: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@pacienteapi.route('/pacientes/<int:paciente_id>', methods=['DELETE'])
def deletePaciente(paciente_id):
    pacientedao = PacienteDao()

    try:
        if pacientedao.deletePaciente(paciente_id):
            return jsonify({
                'success': True,
                'mensaje': f'Paciente con ID {paciente_id} eliminado correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el paciente con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar paciente: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500
