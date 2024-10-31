from flask import current_app as app
from app.conexion.conexion import Conexion
class MedicoDao:

    def _execute_query(self, query, params=None, fetchone=False, commit=False):
        conexion = Conexion()
        with conexion.getConexion() as con:
            with con.cursor() as cur:
                try:
                    cur.execute(query, params or ())
                    if commit:
                        con.commit()
                        return cur.fetchone()[0] if fetchone else cur.rowcount
                    return cur.fetchone() if fetchone else cur.fetchall()
                except Exception as e:
                    app.logger.error(f"Error executing query: {str(e)}")
                    if commit:
                        con.rollback()
                    return None

    def getMedicos(self):
        medicoSQL = "SELECT id, nombre, especialidad, dia, turnos FROM medico"
        medicos = self._execute_query(medicoSQL)
        return [{'id': medico[0], 'nombre': medico[1], 'especialidad': medico[2], 'dia': medico[3], 'turnos': medico[4]} for medico in medicos] if medicos else []

    def getMedicoById(self, medico_id):
        medicoSQL = "SELECT id, nombre, especialidad, dia, turnos FROM medico WHERE id=%s"
        medicoEncontrado = self._execute_query(medicoSQL, (medico_id,), fetchone=True)
        return {
            "id": medicoEncontrado[0],
            "nombre": medicoEncontrado[1],
            "especialidad": medicoEncontrado[2],
            "dia": medicoEncontrado[3],
            "turnos": medicoEncontrado[4]
        } if medicoEncontrado else None

    def guardarMedico(self, nombre, especialidad, dia, turnos):
        insertMedicoSQL = "INSERT INTO medico(nombre, especialidad, dia, turnos) VALUES(%s, %s, %s, %s) RETURNING id"
        return self._execute_query(insertMedicoSQL, (nombre, especialidad, dia, turnos), fetchone=True, commit=True)

    def updateMedico(self, medico_id, nombre, especialidad, dia, turnos):
        updateMedicoSQL = "UPDATE medico SET nombre=%s, especialidad=%s, dia=%s, turnos=%s WHERE id=%s"
        filas_afectadas = self._execute_query(updateMedicoSQL, (nombre, especialidad, dia, turnos, medico_id), commit=True)
        return filas_afectadas > 0

    def deleteMedico(self, medico_id):
        deleteMedicoSQL = "DELETE FROM medico WHERE id=%s"
        rows_affected = self._execute_query(deleteMedicoSQL, (medico_id,), commit=True)
        return rows_affected > 0