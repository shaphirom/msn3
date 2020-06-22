from go import db
from datetime import datetime


class User(db.Model):
    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(30), nullable = False)

    def __repr__(self):
        return f'<User {self.id}>' 


class Message(db.Model):
    __tablename__= 'message'
    id = db.Column(db.Integer, primary_key= True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)
    message = db.Column(db.Text, nullable=False)
    f_sub = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)
    f_mod = db.Column(db.DateTime, nullable = False, onupdate = datetime.utcnow)

    user = db.relationship('User', backref=db.backref('message'), lazy=True)

    def __repr__(self):
        return f'<Message {self.id}>' 
