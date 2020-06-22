from flask import render_template, redirect, flash, url_for
from flask_login import login_required, login_user, logout_user, current_user

from go import app
from forms import RegistroForm, LoginForm, AddMensaje
from models import db, User, Message

@app.route('/')
def index():
    return 'Primera pagina'