from flask import Blueprint, request, jsonify, current_app as app
from app.dao.referenciales.pais.PaisDao import PaisDao

paiapi = Blueprint('paiapi', __name__)

# Trae todas los
@paiapi.route('/paises', methods=['GET'])
def getPaises():
    paidao = PaisDao()

    try:
        paises = paidao.getPais()

        return jsonify({
            'success': True,
            'data': paises,
            'error': None
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener el pais: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@paiapi.route('/paises/<int:pais_id>', methods=['GET'])
def getPais(pais_id):
    paisdao = PaisDao()

    try:
        pais = paisdao.getPaisById(pais_id)

        if pais:
            return jsonify({
                'success': True,
                'data': pais,
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la pais con el ID proporcionado.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al obtener pais: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

# Agrega una nueva ciudad
@paiapi.route('/paises', methods=['POST'])
def addPais():
    data = request.get_json()
    paisdao = PaisDao()

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
        pais_id = paisdao.guardarpais(descripcion)
        if pais_id is not None:
            return jsonify({
                'success': True,
                'data': {'id': pais_id, 'descripcion': descripcion},
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo guardar la ciudad. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al agregar ciudad: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@paiapi.route('/paises/<int:pais_id>', methods=['PUT'])
def updatePais(pais_id):
    data = request.get_json()
    paisdao = PaisDao()

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
        if paisdao.updatePais(pais_id, descripcion):
            return jsonify({
                'success': True,
                'data': {'id': pais_id, 'descripcion': descripcion},
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró la pais con el ID proporcionado o no se pudo actualizar.'
            }), 404
    except Exception as e:
        app.logger.error(f"Error al actualizar pais: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500

@paiapi.route('/paises/<int:pais_id>', methods=['DELETE'])
def deletePais(pais_id):
    paisdao = PaisDao()

    try:
        # Usar el retorno de eliminarCiudad para determinar el éxito
        if paisdao.deletePais(pais_id):
            return jsonify({
                'success': True,
                'mensaje': f'pais con ID {pais_id} eliminada correctamente.',
                'error': None
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'No se encontró el pais con el ID proporcionado o no se pudo eliminar.'
            }), 404

    except Exception as e:
        app.logger.error(f"Error al eliminar pais: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500