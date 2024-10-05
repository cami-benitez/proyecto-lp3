from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.sexo.SexoDao import SexoDao

sexapi = Blueprint('sexapi', __name__)

# Trae todas las ciudades
@sexapi.route('/sexo', methods=['GET'])
def getSexo():
    sexdao = SexoDao()

    try:
        sexo = sexdao.getSexo()

        return jsonify({
            'success': True,
            'data': sexo,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener el sexo: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@sexapi.route('/sexo/<int:sexo_id>', methods=['GET'])
def getSexos(sexo_id):
    sexdao = SexoDao()

    try:
        sexo = sexdao.getSexoById(sexo_id)

        if sexo:
            return jsonify({
                'success': True,
                'data': sexo,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el sexo con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener sexo: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva ciudad
@sexapi.route('/sexo', methods=['POST'])
def addSexo():
    data = request.get_json()
    sexdao = SexoDao()

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
        sexo_id = sexdao.guardarSexo(descripcion)
        if sexo_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': sexo_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar el sexo. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar el sexo: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@sexapi.route('/sexo/<int:sexo_id>', methods=['PUT'])
def updateSexo(sexo_id):
    data = request.get_json()
    sexdao = SexoDao()

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
        if sexdao.updateSexo(sexo_id, descripcion):
            return jsonify({
                'success': True,
                'data': {'id': sexo_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el sexo con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar sexo: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@sexapi.route('/sexo/<int:sexo_id>', methods=['DELETE'])
def deleteSexo(sexo_id):
    sexdao = SexoDao()

    try:
        # Usar el retorno de eliminarCiudad para determinar el éxito
        if sexdao.deleteSexo(sexo_id):
            return jsonify({
                'success': True,
                'mensaje': f'Sexo con ID {sexo_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el sexo con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar sexo: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500