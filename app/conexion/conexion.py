import psycopg2 
class Conexion:
    """Metodo constructor de tu perro
    """
    def __init__(self):
        self.con = psycopg2.connect(dbname="proyecto-lp3", user="postgres", host="localhost", password="6740362")
        """getConexion 
        
        retorno la instalacion de la base de datos 
        """
    def getConexion(self):
        return self.con