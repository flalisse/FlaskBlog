from app import db
from datetime import datetime
from werkzeug import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class User(db.Model, UserMixin):

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64),index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(127))

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):

        return '<User {} >'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))


    def __repr__(self):
        return '<Post {}>'.format(self.body)
#
#class InfoCity(db.Model):
#    id = db.Colunm(db.Integer,primary_key=True)
#   temp = db.Column(db.String(float))
 #   wind = db.Column(db.String(float))
  #  timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

   # def __repr__(self):
    #    return '< temp = {}, wind ={}'.format(self.temp,self.wind)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))



