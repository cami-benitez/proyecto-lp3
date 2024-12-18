from flask import current_app as app
from app.conexion.conexion import Conexion
from app.dao.agenda_medicas.registrar_agenda_medicas.dto.agenda_medica_dto import AgendaMedicaDto 
from app.dao.agenda_medicas.registrar_agenda_medicas.dto.agenda_medica_dto import AgendaMedicaDto

class AgendaMedicaDao:
    
    def obtener_agenda(self):
        query_agenda = """
        SELECT
            am.id_agenda_medica,
            am.id_medico,
            m.nombres medico,
            am.id_especialidad,
            e.descripcion especialidad,
            am.sala_atencion,
            am.turno,
            am.dia
        FROM
            public.agenda_medica am
        LEFT JOIN medicos m
            ON m.id_medico = am.id_medico
        LEFT JOIN especialidades e
            ON e.id_especialidad = am.id_especialidad
        """

        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(query_agenda)
            agenda = cur.fetchall()
            return [{
                    'id_agenda_medica': item[0],
                    'id_medico': item[1],
                    'id_especialidad': item[2],
                    'especialidad': item[3],
                    'sala_atencion': item[4],
                    'turno': item[5],
                    'dia': item[6]
                } for item in agenda]

        except Exception as e:
            app.logger.error(f"Error al obtener la agenda médica: {str(e)}")
        finally:
            cur.close()
            con.close()
        return []

    # agregar
    def agregar(self, agenda_dto: AgendaMedicaDto) -> bool:
        insertAgendaMedica = """
        INSERT INTO public.agenda_medica
        (id_medico, id_especialidad, sala_atencion, turno, dia)
        VALUES(%s, %s, %s, %s, %s)
        RETURNING id_agenda_medica
        """

        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        con.autocommit = False
        cur = con.cursor()
        try:
            # (id_medico, id_especialidad, sala_atencion, turno, dia)
            parametros = (agenda_dto.id_medico, agenda_dto.id_especialidad, agenda_dto.sala_atencion, agenda_dto.turno, agenda_dto.dia)
            cur.execute(insertAgendaMedica, parametros)
            id_agenda_medica = cur.fetchone()[0]

            # Confirma la transacción
            con.commit()
        except Exception as e:
            app.logger.error(f"Error al agregar una nueva agenda médica: {str(e)}")
            con.rollback()
            return False
        finally:
            con.autocommit = True
            cur.close()
            con.close()
        return True

    # modificar
    def modificar(self):
        pass

    # anular
    def anular(self):
        pass
     