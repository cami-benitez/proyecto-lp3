from datetime import date
from flask import Blueprint, jsonify, request, current_app as app
from app.dao.agenda_medicas.registrar_agenda_medicas.AgendaMedicaDao \
    import AgendaMedicaDao
from app.dao.agenda_medicas.registrar_agenda_medicas.dto.agenda_medica_dto\
    import AgendaMedicaDto, AgendaMedicaDetalleDto, EstadoAgendamedica

amapi = Blueprint('amapi', __name__)

@amapi.route('/agenda', methods=['GET'])
def get_agendas():
    dao = AgendaMedicaDao()

    try:
        agenda = dao.obtener_agenda()
        return jsonify({
            'success': True,
            'data': agenda,
            'error': False
        }), 200

    except Exception as e:
        app.logger.error(f"Error al obtener la agenda: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador'
        }), 500
    
@amapi.route('/agenda', methods=['POST'])
def add():
    amdao = AgendaMedicaDao()
    data = request.get_json()
    # Validar que el JSON no esté vacío y tenga las propiedades necesarias
    campos_requeridos = ['id_medico', 'id_especialidad', 'id_turno', 'id_dia', 'sala_atencion']
    # Verificar si faltan campos o son vacíos
    for campo in campos_requeridos:
        if campo not in data or data[campo] is None:
            return jsonify({
                        'success': False,
                        'error': f'El campo {campo} es obligatorio y no puede estar vacío.'
                    }), 400
    try:
        id_medico = data['id_medico']
        id_especialidad = data['id_especialidad']
        id_turno = data['id_turno']
        id_dia = data['id_dia']
        sala_atencion = data['sala_atencion']

        detalle_dto = [AgendaMedicaDetalleDto(
                        id_agenda_medica=None
                        , id_medico=item['id_medico']
                    )for item in detalle_dto]

        cabecera_dto = AgendaMedicaDto(
            id_agenda_medica=None
            , id_medico=id_medico
            , id_especialidad=id_especialidad
            , estado=EstadoAgendamedica(id=2, descripcion=None) # Pendiente
            , id_turno= id_turno
            , id_dia=id_dia
            , sala_atencion=sala_atencion
        )

        resultado = amdao.agregar(agenda_dto=cabecera_dto)
        if resultado:
            return jsonify({
                'success': True,
                'error': None
            }), 201
        else:
            return jsonify({ 'success': False, 'error': 'No se pudo crear la agenda. Consulte con el administrador.' }), 500
    except Exception as e:
        app.logger.error(f"Error al crear agenda: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ocurrió un error interno. Consulte con el administrador.'
        }), 500


