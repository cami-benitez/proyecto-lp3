from flask import Flask

app = Flask(__name__)


#impotar referenciales 
from app.rutas.referenciales.ciudad.ciudad_route import ciumod 

# registrar referenciales 
app.register_blueprint(ciumod, url_prefix='/ciudad')