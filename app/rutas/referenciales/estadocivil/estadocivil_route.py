from flask import Blueprint, render_template

estmod = Blueprint('estadocivil', __name__, template_folder='templates')

@estmod.route('/estadocivil-index')
def estadocivilIndex():
    return render_template('estadocivil-index.html')