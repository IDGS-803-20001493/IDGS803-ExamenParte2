from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_security import login_required, current_user
from flask_security.decorators import roles_required, roles_accepted
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security.utils import login_user, logout_user, hash_password, encrypt_password

from .models import sets
from . import db, userDataStore
import base64

setsLego = Blueprint("setsLego",__name__)

@setsLego.route("/obtenerSets")
def obtenerSets():
    setsObtenidos = sets.query.all()
    return render_template("/security/profile.html", lista = setsObtenidos)

@setsLego.route("/guardar", methods=['GET','POST'])
def guardar():
    idset= str(request.form.get("idSet"))
    nombre = str(request.form.get("nombre"))
    descripcion = str(request.form.get("description"))
    precio = float(request.form.get("precio"))
    imagen = request.files['imagen'].read()
    imagenCodificada = base64.b64encode(imagen)
    
    
    if len(idset) > 0 :
        setElejido = sets.query.filter_by(idSet=int(idset)).first()
        setElejido.nombre = nombre
        setElejido.precio = precio
        setElejido.description = descripcion
        setElejido.imagen = imagenCodificada
        setElejido.estatus=1
        db.session.commit()
    else:
        setGuardado = sets(nombre=nombre, precio = precio, description=descripcion, imagen=imagenCodificada, estatus=1)
        db.session.add(setGuardado)
        db.session.commit()
    
    return redirect(url_for("main.profile"))


@setsLego.route("/eliminar", methods=['GET','POST'])
def eliminar():
    idset= str(request.form.get("idSet2"))

    
    setElejido = sets.query.filter_by(idSet=int(idset)).first()
    setElejido.estatus = 0
    db.session.commit()
    
    return redirect(url_for("main.profile"))

@setsLego.route("/modificar", methods=['GET','POST'])
def modificar():
    idset= str(request.form.get("idSet1"))
    nombre = str(request.form.get("nombre1"))
    descripcion = str(request.form.get("description1"))
    precio = float(request.form.get("precio1"))

    setsObtenidos = sets.query.all()
    return render_template("profile.html", name=current_user.name, lista = setsObtenidos, idSet=idset, nombre=nombre, descripcion=descripcion, precio=precio)
    
