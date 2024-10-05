from flask import current_app as app
from app.conexion.conexion import Conexion

class EstadocivilDao:

    def getEstadocivil(self):

        estadocivilSQL = """
        SELECT id, descripcion
        FROM estadocivil
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(estadocivilSQL)
            estadocivil = cur.fetchall() # trae datos de la bd
            
            # Transformar los datos en una lista de diccionarios
            return [{'id': estadocivil[0], 'descripcion': estadocivil[1]} for estadocivil in estadocivil]
        except Exception as e:
            app.logger.error(f"Error al obtener el estadocivil: {str(e)}")
            return []    
        finally:
            cur.close()
            con.close()

    def getEstadocivilById(self, id):

        estadocivilSQL = """
        SELECT id, descripcion
        FROM estadocivil WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(estadocivilSQL, (id,))
            estadocivilEncontrada = cur.fetchone() # Obtener una sola fila
            if estadocivilEncontrada:
                return {
                        "id": estadocivilEncontrada[0],
                        "descripcion": estadocivilEncontrada[1]
                    }  # Retornar los datos de la ciudad
            else:
                return None # Retornar None si no se encuentra la ciudad
        except Exception as e:
            app.logger.error(f"Error al obtener estadocivil: {str(e)}")
            return None
        finally:
            cur.close()
            con.close()

    def guardarEstadocivil(self, descripcion):

        insertEstadocivilSQL = """
        INSERT INTO estadocivil(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertEstadocivilSQL, (descripcion,))
            estadocivil_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return estadocivil_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar estadocivil: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False


        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()


    def updateEstadocivil(self, id, descripcion):

        updateEstadocivilSQL = """
        UPDATE estadocivil
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateEstadocivilSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila   
        except Exception as e:
            app.logger.error(f"Error al actualizar estadocivil: {str(e)}")
            con.rollback()
            return False
       
        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()


    def deleteEstadocivil(self, id):

        updateEstadocivilSQL = """
        DELETE FROM estadocivil
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateEstadocivilSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila 

        except Exception as e:
            app.logger.error(f"Error al eliminar estadocivil: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()