from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

db = SQLAlchemy()

class User(db.Model,UserMixin):
    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False, unique=True)
    password_hash = db.Column(db.String(30), nullable = False)
    is_admin = db.Column(db.Boolean, default=False)
    message = db.relationship('Message', backref=db.backref('user'), lazy='dynamic')

    def __repr__(self):
        return f'<User {self.id}>' 

    @property
    def password(self):
        raise AttributeError('password no es un atributo leible')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    

class Message(db.Model):
    __tablename__= 'message'
    id = db.Column(db.Integer, primary_key= True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)
    message = db.Column(db.Text, nullable=False)
    f_sub = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)
    f_mod = db.Column(db.DateTime, nullable = False, default= datetime.utcnow, onupdate = datetime.utcnow)

    def __repr__(self):
        return f'<Message {self.id}>' 
