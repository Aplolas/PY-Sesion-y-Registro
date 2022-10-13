from sesion_y_registro import app
from sesion_y_registro.models.usuario import Usuario
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def raiz():
    return render_template("formularios.html")

@app.route('/creer', methods=['POST'])
def creer():

    if not Usuario.validate(request.form):
        return redirect ('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password" : pw_hash
    }

    user_id = Usuario.save(data)

    session['user_id'] = user_id
    return redirect(f'/bonjour/{session["user_id"]}')

@app.route('/bonjour/<int:id>')
def bonjour(id):
    data = {
        "identificador":id
    }
    usuario = Usuario.get_user(data)
    print(usuario)
    all_users = Usuario.all_users()
    return render_template("bonjour.html", all_ussers=all_users, usuario=usuario)

@app.route('/login',methods=['POST'])
def login():

    data = { "email" : request.form["email"] }
    user_db = Usuario.obtener_x_mail(data)

    if not user_db:
        flash("Email/Mot de passe non valide")
        return redirect("/")
    if not bcrypt.check_password_hash(user_db.password, request.form['password']):

        flash("Email/Mot de passe non valide")
        return redirect('/')

    session['user_id'] = user_db.id
    return redirect(f'/bonjour/{session["user_id"]}')

@app.route('/clearsession')
def clear():
    session.clear()
    return redirect('/')