from flask import current_app as app
from app.conexion.conexion import Conexion

class HorarioDao:

    def getHorario(self):

        horarioSQL = """
        SELECT id, descripcion
        FROM horario
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(horarioSQL)
            horario = cur.fetchall() # trae datos de la bd
            
            # Transformar los datos en una lista de diccionarios
            return [{'id': horario[0], 'descripcion': horario[1]} for horario in horario]
        except Exception as e:
            app.logger.error(f"Error al obtener horario: {str(e)}")
            return []    
        finally:
            cur.close()
            con.close()

    def getHorarioById(self, id):

        horarioSQL = """
        SELECT id, descripcion
        FROM horario WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(horarioSQL, (id,))
            horarioEncontrada = cur.fetchone() # Obtener una sola fila
            if horarioEncontrada:
                return {
                        "id": horarioEncontrada[0],
                        "descripcion": horarioEncontrada[1]
                    }  # Retornar los datos de la ciudad
            else:
                return None # Retornar None si no se encuentra la ciudad
        except Exception as e:
            app.logger.error(f"Error al obtener horario: {str(e)}")
            return None
        finally:
            cur.close()
            con.close()

    def guardarHorario(self, descripcion):

        insertHorarioSQL = """
        INSERT INTO horario(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertHorarioSQL, (descripcion,))
            horario_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return horario_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar horario: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False


        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()


    def updateHorario(self, id, descripcion):

        updateHorarioSQL = """
        UPDATE horario
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateHorarioSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila   
        except Exception as e:
            app.logger.error(f"Error al actualizar horario: {str(e)}")
            con.rollback()
            return False
       
        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()


    def deleteHorario(self, id):

        updateHorarioSQL = """
        DELETE FROM horario
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateHorarioSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila 

        except Exception as e:
            app.logger.error(f"Error al eliminar horario: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()