from flask import Blueprint, render_template
from flask_security import login_required, current_user
from flask_security.decorators import roles_required, roles_accepted
from . import db
from .models import sets

main = Blueprint("main",__name__)

#Definimos la ruta para la página principal
@main.route("/")
def index():
    return render_template("index.html")

@main.route("/comentarios")
def comentarios():
    return render_template("comentarios.html")

#Definimos la ruta para la página perfil de usuario
@main.route("/profile")
@login_required
#@roles_required('')
@roles_accepted('admin','user')

def profile():
    setsObtenidos = sets.query.all()
    return render_template("profile.html", name=current_user.name, lista = setsObtenidos, idSet="", nombre="", descripcion="", precio="")


