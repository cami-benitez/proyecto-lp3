# Data access object - DAO
from flask import current_app as app
from app.conexion.conexion import Conexion

class PersonaDao:

    def getPersona(self):

        personaSQL = """
        SELECT id, descripcion, apellido, numero_cedula
        FROM personas
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(personaSQL)
            personas = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': persona[0], 'descripcion': persona[1], 'apellido': persona[2], 'cedula': persona[3]} for persona in personas]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las personas: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getPersonaById(self, id):

        personaSQL = """
        SELECT id, descripción, apellido, numero_cedula
        FROM personas WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(personaSQL, (id,))
            personaEncontrada = cur.fetchone() # Obtener una sola fila
            if personaEncontrada:
                return {
                        "id": personaEncontrada[0],
                        "descripcion": personaEncontrada[1],
                        "apellido": personaEncontrada[2],
                        "numero_cedula": personaEncontrada[3],
                    }  # Retornar los datos de la persona
            else:
                return None # Retornar None si no se encuentra la persona
        except Exception as e:
            app.logger.error(f"Error al obtener persona: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarPersona(self, descripcion, apellido, numero_cedula):

        insertPersonaSQL = """
   INSERT INTO personas(descripción, apellido, numero_cedula) VALUES(%s, %s,%s) RETURNING id        
   """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertPersonaSQL, (descripcion, apellido, numero_cedula))
            persona_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return persona_id
        
        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar persona: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

          # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updatePersona(self,id, descripcion, apellido, numero_cedula):

        updatePersonaSQL = """
        UPDATE personas
        SET descripcion=%s
        SET apellido=%s
        SET numero_cedula=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updatePersonaSQL, (apellido, numero_cedula, descripcion, id))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas            con.commit()
            con.commit()
        
            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar persona: {str(e)}")
            con.rollback()
            return False 
               
        finally:
            cur.close()
            con.close()

    def deletePersona(self, id):

        updatePersonaSQL = """
        DELETE FROM personas
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updatePersonaSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila        
        except Exception as e:
            app.logger.error(f"Error al eliminar persona: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()