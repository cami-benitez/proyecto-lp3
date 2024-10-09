from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.persona.PersonaDao import PersonaDao

perapi = Blueprint('perapi', __name__)

# Trae todas las ciudades
@perapi.route('/persona', methods=['GET'])
def getPersona():
    perdao = PersonaDao()

    try:
        persona = perdao.getPersona()

        return jsonify({
            'success': True,
            'data': persona,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener todas las persona: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@perapi.route('/persona/<int:persona_id>', methods=['GET'])
def getPersonas(persona_id):
    perdao = PersonaDao()

    try:
        persona = perdao.getPersonaById(persona_id)

        if persona:
            return jsonify({
                'success': True,
                'data': persona,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la persona con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener persona: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva ciudad
@perapi.route('/persona', methods=['POST'])
def addPersona():
    data = request.get_json()
    perdao = PersonaDao()

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
        persona_id = perdao.guardarPersona(descripcion)
        if persona_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': persona_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la persona. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar persona: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@perapi.route('/persona/<int:persona_id>', methods=['PUT'])
def updatePersona(persona_id):
    data = request.get_json()
    perdao = PersonaDao()

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
        if perdao.updatePersona(persona_id, descripcion):
            return jsonify({
                'success': True,
                'data': {'id': persona_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la persona con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar persona: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@perapi.route('/persona/<int:persona_id>', methods=['DELETE'])
def deletePersona(persona_id):
    perdao = PersonaDao()

    try:
        # Usar el retorno de eliminarCiudad para determinar el éxito
        if perdao.deletePersona(persona_id):
            return jsonify({
                'success': True,
                'mensaje': f'persona con ID {persona_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la persona con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar persona: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500