from flask import Blueprint, render_template
from app.dao.referenciales.Dia.DiaDao import DiaDao
from app.dao.referenciales.turno.TurnoDao import TurnoDao
from app.dao.referenciales.Medico.MedicoDao import MedicoDao

ammod = Blueprint('ammod', __name__, template_folder='templates')

@ammod.route('/agenda-index')
def agenda_index():
    return render_template('agenda-index.html')

@ammod.route('/agenda-agregar')
def agenda_agregar():
    meddao = MedicoDao()

    return render_template('agenda-agregar.html'\
        , medico = meddao.get_medico())