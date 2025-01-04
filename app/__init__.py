from flask import Flask

app = Flask(__name__)


#impotar referenciales 
from app.rutas.referenciales.ciudad.ciudad_route import ciumod 
from app.rutas.referenciales.pais.pais_route import paimod
from app.rutas.referenciales.persona.persona_route import persona_mod
from app.rutas.referenciales.paciente.paciente_route import pacientemod
from app.rutas.referenciales.dia.dia_route import diamod
from app.rutas.referenciales.turno.turno_route import turmod
from app.rutas.referenciales.genero.genero_route import genmod
from app.rutas.referenciales.diagnostico.diagnostico_route import diagmod
from app.rutas.referenciales.estadocivil.estadocivil_route import estmod
from app.rutas.referenciales.enfermedad.enfermedad_route import enfmod
from app.rutas.referenciales.ocupacion.ocupacion_route import ocumod
from app.rutas.referenciales.cita.cita_route import citmod
from app.rutas.referenciales.medico.medico_route import medico_mod
from app.rutas.referenciales.pago.pago_route import pagmod
from app.rutas.referenciales.horario.horario_route import hormod
from app.rutas.referenciales.servicio.servicio_route import sermod


# registrar referenciales 
modulo0 ='/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')

from app.rutas.referenciales.ciudad.ciudad_api import ciuapi

# importar agenda medica
from app.rutas.registrar_agenda_medica.registrar_agenda_medica_route import ammod 
# registro de modulo 
modulo1 ='/agenda-medica'
app.register_blueprint(ammod, url_prefix=f'{modulo1}/registrar-agenda-medica')

from app.rutas.registrar_agenda_medica.registar_agenda_medica_api import amapi


# APIS v1
modulo0 ='/referenciales'
app.register_blueprint(paimod, url_prefix=f'{modulo0}/pais')

from app.rutas.referenciales.pais.pais_api import paiapi

modulo0 = '/referenciales'
app.register_blueprint(persona_mod, url_prefix=f'{modulo0}/persona')

from app.rutas.referenciales.persona.persona_api import personaapi

modulo0 = '/referenciales'
app.register_blueprint(pacientemod, url_prefix=f'{modulo0}/paciente')

from app.rutas.referenciales.paciente.paciente_api import pacienteapi

modulo0 = '/referenciales'
app.register_blueprint(diamod, url_prefix=f'{modulo0}/dia')

from app.rutas.referenciales.dia.dia_api import diaapi

modulo0 = '/referenciales'
app.register_blueprint(turmod, url_prefix=f'{modulo0}/turno')

from app.rutas.referenciales.turno.turno_api import turapi

modulo0 = '/referenciales'
app.register_blueprint(genmod, url_prefix=f'{modulo0}/genero')

from app.rutas.referenciales.genero.genero_api import genapi

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
app.register_blueprint(medico_mod, url_prefix=f'{modulo0}/Medico')

from app.rutas.referenciales.medico.medico_api import medico_api

modulo0 = '/referenciales'
app.register_blueprint(pagmod, url_prefix=f'{modulo0}/Pago')

from app.rutas.referenciales.pago.pago_api import pagapi

modulo0 = '/referenciales'
app.register_blueprint(hormod, url_prefix=f'{modulo0}/Horario')

from app.rutas.referenciales.horario.horario_api import horapi

modulo0 = '/referenciales'
app.register_blueprint(sermod, url_prefix=f'{modulo0}/Servicio')

from app.rutas.referenciales.servicio.servicio_api import serapi

version1 = '/api/v1'
app.register_blueprint(ciuapi, url_prefix=version1)

app.register_blueprint(paiapi, url_prefix=version1)

app.register_blueprint(personaapi, url_prefix=version1)

app.register_blueprint(pacienteapi, url_prefix=version1)

app.register_blueprint(diaapi, url_prefix=version1)

app.register_blueprint(turapi, url_prefix=version1)

app.register_blueprint(genapi, url_prefix=version1)

app.register_blueprint(diagapi, url_prefix=version1)

app.register_blueprint(estapi, url_prefix=version1)

app.register_blueprint(enfapi, url_prefix=version1)

app.register_blueprint(ocuapi, url_prefix=version1)

app.register_blueprint(citapi, url_prefix=version1)

app.register_blueprint(medico_api, url_prefix=version1)

app.register_blueprint(pagapi, url_prefix=version1)

app.register_blueprint(horapi, url_prefix=version1)

app.register_blueprint(serapi, url_prefix=version1)

apiversion1 = '/api/v1'
#agenda api
app.register_blueprint(amapi, url_prefix=f'{apiversion1}/{modulo1}/registrar-agenda-medica')
