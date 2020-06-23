from flask import render_template, redirect, flash, url_for
from flask_login import login_required, login_user, logout_user, current_user

from go import app
from forms import RegistroForm, LoginForm, AddMensaje
from models import db, User, Message

@app.route('/')
def index():
    return render_template('index.html', register_form = RegistroForm(), login_form=LoginForm())

@app.route('/registro/', methods = ['GET','POST'])
def register():
    form = RegistroForm()

    if form.validate_on_submit():
        form.validate_email(form.email)
        print(form.nombre.data)
        print(form.email.data)
        print(form.password.data)
        user = User(name = form.nombre.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Tu cuenta ha sido creada.')
        return redirect('/login')

    return render_template('register.html', form = form)


@app.route('/login/', methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=True)

            return redirect(url_for('get_mensajes'))
        flash('Email o Password Incorrectos')
    return render_template('login.html',form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('Acabas de cerrar sesion')
    return redirect(url_for('login'))


@app.route('/mensaje/<int:id>')
@login_required
def get_mensaje(id):
    mensaje = Message.query.filter_by(id=id).first()
    mensajes = Message.query.filter_by(user=current_user).all()

    if mensaje is None:
        return render_template('404.html'), 404

    if mensaje.user is None:
        return render_template('403.html'), 403

    return render_template('mensaje.html', mensaje =mensaje, mensajes = mensajes)

@app.route('/mensaje')
@login_required
def get_mensajes():
    mensajes = Message.query.filter_by(user=current_user).all()
    return render_template('mensajes.html', mensajes=mensajes)


@app.route('/add_mensaje', methods=['GET','POST'])
@login_required
def add_mensaje():
    form = AddMensaje()

    if form.validate_on_submit():
        mensaje = Message(message= form.mensaje.data)
        mensaje.user = current_user

        db.session.add(mensaje)
        db.session.commit()

        flash('El mensaje fue grabado correctamente')
        return redirect(url_for('get_mensajes'))

    return render_template('add_mensaje.html',form = form)