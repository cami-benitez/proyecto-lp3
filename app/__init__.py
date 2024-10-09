from flask import Flask

app = Flask(__name__)


#impotar referenciales 
from app.rutas.referenciales.ciudad.ciudad_route import ciumod 
from app.rutas.referenciales.pais.pais_route import paimod
from app.rutas.referenciales.persona.persona_route import permod
from app.rutas.referenciales.dia.dia_route import diamod
from app.rutas.referenciales.turno.turno_route import turmod
from app.rutas.referenciales.sexo.sexo_route import sexmod
from app.rutas.referenciales.diagnostico.diagnostico_route import diagmod
from app.rutas.referenciales.estadocivil.estadocivil_route import estmod
from app.rutas.referenciales.enfermedad.enfermedad_route import enfmod
from app.rutas.referenciales.ocupacion.ocupacion_route import ocumod
from app.rutas.referenciales.cita.cita_route import citmod
from app.rutas.referenciales.medico.medico_route import medmod
from app.rutas.referenciales.pago.pago_route import pagmod
from app.rutas.referenciales.horario.horario_route import hormod
from app.rutas.referenciales.servicio.servicio_route import sermod



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

modulo0 = '/referenciales'
app.register_blueprint(sexmod, url_prefix=f'{modulo0}/sexo')

from app.rutas.referenciales.sexo.sexo_api import sexapi

modulo0 = '/referenciales'
app.register_blueprint(diagmod, url_prefix=f'{modulo0}/Diagnostico')

from app.rutas.referenciales.diagnostico.diagnostico_api import diagapi

modulo0 = '/referenciales'
app.register_blueprint(estmod, url_prefix=f'{modulo0}/Estadocivil')

from app.rutas.referenciales.estadocivil.estadocivil_api import estapi

modulo0 = '/referenciales'
app.register_blueprint(enfmod, url_prefix=f'{modulo0}/Enfermedad')

from app.rutas.referenciales.enfermedad.enfermedad_api import enfapi

modulo0 = '/referenciales'
app.register_blueprint(ocumod, url_prefix=f'{modulo0}/ocupacion')

from app.rutas.referenciales.ocupacion.ocupacion_api import ocuapi

modulo0 = '/referenciales'
app.register_blueprint(citmod, url_prefix=f'{modulo0}/citas')

from app.rutas.referenciales.cita.cita_api import citapi

modulo0 = '/referenciales'
app.register_blueprint(medmod, url_prefix=f'{modulo0}/Medico')

from app.rutas.referenciales.medico.medico_api import medapi

modulo0 = '/referenciales'
app.register_blueprint(pagmod, url_prefix=f'{modulo0}/Pago')

from app.rutas.referenciales.pago.pago_api import pagapi

modulo0 = '/referenciales'
app.register_blueprint(hormod, url_prefix=f'{modulo0}/Horario')

from app.rutas.referenciales.horario.horario_api import horapi

modulo0 = '/referenciales'
app.register_blueprint(sermod, url_prefix=f'{modulo0}/Servicio')

from app.rutas.referenciales.servicio.servicio_api import serapi

# APIS v1
version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)

app.register_blueprint(paiapi, url_prefix=version1)

app.register_blueprint(perapi, url_prefix=version1)

app.register_blueprint(diaapi, url_prefix=version1)

app.register_blueprint(turapi, url_prefix=version1)

app.register_blueprint(sexapi, url_prefix=version1)

app.register_blueprint(diagapi, url_prefix=version1)

app.register_blueprint(estapi, url_prefix=version1)

app.register_blueprint(enfapi, url_prefix=version1)

app.register_blueprint(ocuapi, url_prefix=version1)

app.register_blueprint(citapi, url_prefix=version1)

app.register_blueprint(medapi, url_prefix=version1)

app.register_blueprint(pagapi, url_prefix=version1)

app.register_blueprint(horapi, url_prefix=version1)

app.register_blueprint(serapi, url_prefix=version1)
