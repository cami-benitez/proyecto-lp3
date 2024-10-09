from flask import current_app as app
from app.conexion.conexion import Conexion

class PagoDao:

    def getPago(self):

        pagoSQL = """
        SELECT id, descripcion
        FROM pago
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(pagoSQL)
            pago = cur.fetchall() # trae datos de la bd
            
            # Transformar los datos en una lista de diccionarios
            return [{'id': pago[0], 'descripcion': pago[1]} for pago in pago]
        except Exception as e:
            app.logger.error(f"Error al obtener metodo: {str(e)}")
            return []    
        finally:
            cur.close()
            con.close()

    def getPagoById(self, id):

        pagoSQL = """
        SELECT id, descripcion
        FROM pago WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(pagoSQL, (id,))
            pagoEncontrada = cur.fetchone() # Obtener una sola fila
            if pagoEncontrada:
                return {
                        "id": pagoEncontrada[0],
                        "descripcion": pagoEncontrada[1]
                    }  # Retornar los datos de la ciudad
            else:
                return None # Retornar None si no se encuentra la ciudad
        except Exception as e:
            app.logger.error(f"Error al obtener metodo: {str(e)}")
            return None
        finally:
            cur.close()
            con.close()

    def guardarPago(self, descripcion):

        insertPagoSQL = """
        INSERT INTO pago(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertPagoSQL, (descripcion,))
            pago_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return pago_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar metodo: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False


        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()


    def updatePago(self, id, descripcion):

        updatePagoSQL = """
        UPDATE pago
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updatePagoSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila   
        except Exception as e:
            app.logger.error(f"Error al actualizar metodo: {str(e)}")
            con.rollback()
            return False
       
        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()


    def deletePago(self, id):

        updatePagoSQL = """
        DELETE FROM pago
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updatePagoSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila 

        except Exception as e:
            app.logger.error(f"Error al eliminar metodo: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()