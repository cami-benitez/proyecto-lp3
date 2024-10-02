from flask import Flask

app = Flask(__name__)


#impotar referenciales 
from app.rutas.referenciales.ciudad.ciudad_route import ciumod 
from app.rutas.referenciales.pais.pais_route import paimod
from app.rutas.referenciales.persona.persona_route import permod

# registrar referenciales 
modulo0 ='/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')

from app.rutas.referenciales.ciudad.ciudad_api import ciuapi


modulo0 ='/referenciales'
app.register_blueprint(paimod, url_prefix=f'{modulo0}/pais')

from app.rutas.referenciales.pais.pais_api import paiapi

modulo0 = '/referenciales'
app.register_blueprint(permod, url_prefix=f'{modulo0}/persona')

from app.rutas.referenciales.persona.persona_api import perapi

# APIS v1
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(paiapi, url_prefix=version1)

version1 = '/api/v1'
app.register_blueprint(perapi, url_prefix=version1)
