from flask import current_app as app
from app.conexion.conexion import Conexion

class CitaDao:

    def getCita(self):

        citaSQL = """
        SELECT id, descripcion
        FROM cita
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(citaSQL)
            cita = cur.fetchall() # trae datos de la bd
            
            # Transformar los datos en una lista de diccionarios
            return [{'id': cita[0], 'descripcion': cita[1]} for cita in cita]
        except Exception as e:
            app.logger.error(f"Error al obtener todas las cita: {str(e)}")
            return []    
        finally:
            cur.close()
            con.close()

    def getCitaById(self, id):

        citaSQL = """
        SELECT id, descripcion
        FROM cita WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(citaSQL, (id,))
            citaEncontrada = cur.fetchone() # Obtener una sola fila
            if citaEncontrada:
                return {
                        "id": citaEncontrada[0],
                        "descripcion": citaEncontrada[1]
                    }  # Retornar los datos de la ciudad
            else:
                return None # Retornar None si no se encuentra la ciudad
        except Exception as e:
            app.logger.error(f"Error al obtener cita: {str(e)}")
            return None
        finally:
            cur.close()
            con.close()

    def guardarCita(self, descripcion):

        insertCitaSQL = """
        INSERT INTO cita(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertCitaSQL, (descripcion,))
            cita_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return cita_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar cita: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False


        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()


    def updateCita(self, id, descripcion):

        updateCitaSQL = """
        UPDATE cita
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateCitaSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila   
        except Exception as e:
            app.logger.error(f"Error al actualizar cita: {str(e)}")
            con.rollback()
            return False
       
        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()


    def deleteCita(self, id):

        updateCitaSQL = """
        DELETE FROM cita
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateCitaSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila 

        except Exception as e:
            app.logger.error(f"Error al eliminar cita: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()