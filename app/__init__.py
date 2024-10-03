from flask import Flask

app = Flask(__name__)


#impotar referenciales 
from app.rutas.referenciales.ciudad.ciudad_route import ciumod 
from app.rutas.referenciales.pais.pais_route import paimod
from app.rutas.referenciales.persona.persona_route import permod
from app.rutas.referenciales.dia.dia_route import diamod
from app.rutas.referenciales.turno.turno_route import turmod

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

modulo0 = '/referenciales'
app.register_blueprint(diamod, url_prefix=f'{modulo0}/dia')

from app.rutas.referenciales.dia.dia_api import diaapi

modulo0 = '/referenciales'
app.register_blueprint(turmod, url_prefix=f'{modulo0}/turno')

from app.rutas.referenciales.turno.turno_api import turapi

# APIS v1
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)

app.register_blueprint(paiapi, url_prefix=version1)

app.register_blueprint(perapi, url_prefix=version1)

app.register_blueprint(diaapi, url_prefix=version1)

app.register_blueprint(turapi, url_prefix=version1)
