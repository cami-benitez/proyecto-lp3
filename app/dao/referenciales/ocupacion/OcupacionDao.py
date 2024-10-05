from flask import current_app as app
from app.conexion.conexion import Conexion

class OcupacionDao:

    def getOcupacion(self):

        ocupacionSQL = """
        SELECT id, descripcion
        FROM ocupacion
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(ocupacionSQL)
            ocupacion = cur.fetchall() # trae datos de la bd
            
            # Transformar los datos en una lista de diccionarios
            return [{'id': ocupacion[0], 'descripcion': ocupacion[1]} for ocupacion in ocupacion]
        except Exception as e:
            app.logger.error(f"Error al obtener todas lasocupacion: {str(e)}")
            return []    
        finally:
            cur.close()
            con.close()

    def getocupacionById(self, id):

        ocupacionSQL = """
        SELECT id, descripcion
        FROM ocupacion WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(ocupacionSQL, (id,))
            ocupacionEncontrada = cur.fetchone() # Obtener una sola fila
            if ocupacionEncontrada:
                return {
                        "id": ocupacionEncontrada[0],
                        "descripcion": ocupacionEncontrada[1]
                    }  # Retornar los datos de la ciudad
            else:
                return None # Retornar None si no se encuentra la ciudad
        except Exception as e:
            app.logger.error(f"Error al obtener ocupacion: {str(e)}")
            return None
        finally:
            cur.close()
            con.close()

    def guardarOcupacion(self, descripcion):

        insertOcupacionSQL = """
        INSERT INTO ocupacion(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertOcupacionSQL, (descripcion,))
            ocupacion_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return ocupacion_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar ocupacion: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False


        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()


    def updateOcupacion(self, id, descripcion):

        updateOcupacionSQL = """
        UPDATE ocupacion
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateOcupacionSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila   
        except Exception as e:
            app.logger.error(f"Error al actualizar ocupacion: {str(e)}")
            con.rollback()
            return False
       
        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()


    def deleteOcupacion(self, id):

        updateOcupacionSQL = """
        DELETE FROM ocupacion
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateOcupacionSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila 

        except Exception as e:
            app.logger.error(f"Error al eliminar ocupacion: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()