from os.path import abspath, dirname, join

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from models import db, User, Message 

basedir = abspath(dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % join(basedir,'msn3.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

import views

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.cli.command()
def create_all():
    """Crear todas las tablas"""
    db.create_all()