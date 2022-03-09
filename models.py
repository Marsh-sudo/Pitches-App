
from app import db
from flask_login import UserMixin, current_user
# from flask_login import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    upvotes = db.relationship('upvote',backref = 'user',lazy = "dynamic")
    downvotes = db.relationship('downvote' ,backref = 'user',lazy="dynamic")
    pitch = db.relationship('Pitch',backref = 'user', lazy = "dynamic")
    comments = db.relationship('Comments',backref = 'user', lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return  f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    category = db.Column(db.String(255))
    comments = db.relationship('Comment',backref = 'pitch',lazy = "dynamic")
    downvotes = db.relationship('downvotes',backref = 'pitch',lazy = "dynamic")
    upvotes = db.relationship('upvotes',backref = 'pitch',lazy = "dynamic")
    

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls,id):
        pitch = Pitch.query.filter_by(pitch_id=id).all
        return pitch

    def __repr__(self):
        return f'User {self.description}'


class Comment:
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitch.id"))
    posted = db.Column(db.DateTime,default = datetime.utcnow)


class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key = True)
    upvote = db.Column(db.Integer,default = 0)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))


    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()

    def add_upvotes(cls,id):
        upvote = Upvote(pitch_id=id ,user= current_user)
        return upvote

    @classmethod
    def get_upvotes(cls,id):
        upvotes = Upvote.query.filter_by(pitch_id=id).all()
        return upvotes


    def __repr__(self):
        return f'{self.pitch_id} : {self.user_id}'


class Downvotes(db.Model):

    __tablename__= 'downvotes'

    id = db.Column(db.Integer,primary_key = True)
    downvote = db.Column(db.Integer,default = 0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

    def save_downvotes(self):
        db.session.add(self)
        db.session.commit()

    def add_downvotes(cls,id):
        downvote = Downvotes(pitch_id=id,user = current_user)
        return downvote

    @classmethod
    def get_downvotes(cls,id):
        downvotes = Downvotes.query.filter_by(pitch_id=id).all()
        return downvotes

    def __repr__(self):
        return f'{self.pitch_id} : {self.user_id}'