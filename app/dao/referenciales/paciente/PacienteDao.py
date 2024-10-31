
from flask import current_app as app
from app.conexion.conexion import Conexion

class PacienteDao:

    def getPacientes(self):
        pacienteSQL = """
        SELECT  p.id, pe.nombre,pe.apellido,pe.cedula,p.edad, p.peso, p.altura, pe.id 
        FROM pacientes p, personas pe 
        where p.id_persona = pe.id
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(pacienteSQL)
            pacientes = cur.fetchall()

            # Transformar los datos en una lista de diccionarios con los nuevos campos
            return [{'id': paciente[0], 'nombre': paciente[1], 'apellido': paciente[2], 'cedula': paciente[3], 'edad': paciente[4],'peso': paciente[5], 'altura': paciente[6], 'idpe': paciente[7]} for paciente in pacientes]

        except Exception as e:
            app.logger.error(f"Error al obtener todos los pacientes: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getPacienteById(self, id):
        pacienteSQL = """
        SELECT  p.id, pe.nombre,pe.apellido,pe.cedula,p.edad, p.peso, p.altura,pe.id 
        FROM pacientes p, personas pe 
        where p.id_persona = pe.id and p.id = %s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(pacienteSQL, (id,))
            pacienteEncontrado = cur.fetchone()
            if pacienteEncontrado:
                return {
                    "id": pacienteEncontrado[0],
                    "nombre": pacienteEncontrado[1],
                    "apellido": pacienteEncontrado[2],
                    "cedula": pacienteEncontrado[3],
                    "edad": pacienteEncontrado[4],
                    "peso": pacienteEncontrado[5],
                    "altura": pacienteEncontrado[6],
                    "idpe": pacienteEncontrado[7]
                }
            else:
                return None
        except Exception as e:
            app.logger.error(f"Error al obtener paciente por ID: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarPaciente(self, idpe, edad, peso, altura):
        insertPacienteSQL = """
        INSERT INTO pacientes(id_persona, edad, peso, altura) 
        VALUES(%s, %s, %s, %s) RETURNING id
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(insertPacienteSQL, (idpe, edad, peso, altura))
            paciente_id = cur.fetchone()[0]
            con.commit()
            return paciente_id

        except Exception as e:
            app.logger.error(f"Error al insertar paciente: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def updatePaciente(self, id, idpe, edad, peso, altura):
        updatePacienteSQL = """
        UPDATE pacientes
        SET id_persona=%s, edad=%s, peso=%s, altura=%s
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updatePacienteSQL, (idpe, edad, peso, altura, id))
            filas_afectadas = cur.rowcount
            con.commit()
            return filas_afectadas > 0

        except Exception as e:
            app.logger.error(f"Error al actualizar paciente: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deletePaciente(self, id):
        deletePacienteSQL = """
        DELETE FROM pacientes
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deletePacienteSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0

        except Exception as e:
            app.logger.error(f"Error al eliminar paciente: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()
