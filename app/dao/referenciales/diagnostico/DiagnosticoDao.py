from flask import current_app as app
from app.conexion.conexion import Conexion

class DiagnosticoDao:

    def getDiagnostico(self):

        diagnosticoSQL = """
        SELECT id, descripcion
        FROM diagnostico
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(diagnosticoSQL)
            diagnostico = cur.fetchall() # trae datos de la bd
            
            # Transformar los datos en una lista de diccionarios
            return [{'id': diagnostico[0], 'descripcion': diagnostico[1]} for diagnostico in diagnostico]
        except Exception as e:
            app.logger.error(f"Error al obtener todas el diagnostico: {str(e)}")
            return []    
        finally:
            cur.close()
            con.close()

    def getDiagnosticoById(self, id):

        diagnosticoSQL = """
        SELECT id, descripcion
        FROM diagnostico WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(diagnosticoSQL, (id,))
            diagnosticoEncontrada = cur.fetchone() # Obtener una sola fila
            if diagnosticoEncontrada:
                return {
                        "id": diagnosticoEncontrada[0],
                        "descripcion": diagnosticoEncontrada[1]
                    }  # Retornar los datos de la ciudad
            else:
                return None # Retornar None si no se encuentra la ciudad
        except Exception as e:
            app.logger.error(f"Error al obtener ciudad: {str(e)}")
            return None
        finally:
            cur.close()
            con.close()

    def guardarDiagnostico(self, descripcion):

        insertDiagnosticoSQL = """
        INSERT INTO diagnostico(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertDiagnosticoSQL, (descripcion,))
            diagnostico_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return diagnostico_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar diagnostico: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False


        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()


    def updateDiagnostico(self, id, descripcion):

        updateDiagnosticoSQL = """
        UPDATE diagnostico
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateDiagnosticoSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila   
        except Exception as e:
            app.logger.error(f"Error al actualizar diagnostico: {str(e)}")
            con.rollback()
            return False
       
        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()


    def deleteDiagnostico(self, id):

        updateDiagnosticoSQL = """
        DELETE FROM diagnostico
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateDiagnosticoSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila 

        except Exception as e:
            app.logger.error(f"Error al eliminar diagnostico: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()