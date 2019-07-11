from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from . import db, login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    comment = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    code = db.relationship('Code',backref = 'user',lazy = "dynamic")
    quiz = db.relationship('Quiz',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'

    
class Code(db.Model):
    __tablename__ = 'codes'
    id = db.Column(db.Integer, primary_key=True)
    code_title = db.Column(db.String)
    code = db.Column(db.String)
    code_upvotes = db.Column(db.Integer)
    code_downvotes = db.Column(db.Integer)
    category = db.Column(db.Integer)
    posted = db.Column(db.Time, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    def save_code(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_code(cls, id):
        code = Code.query.filter_by(id=id).first()
        return code


    @classmethod
    def get_codes(cls, id):
        codes = Code.query.filter_by(id=id).all()
        return codes

    def delete_code(self):
        db.session.delete(self)
        db.session.commit()


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db. Integer, primary_key=True)
    comment = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    code_id = db.Column(db.Integer, db.ForeignKey("codes.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    quiz_id = db.Column(db.Integer, db.ForeignKey("quizes.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comments = Comment.query.filter_by(code_id=id).all()
        return comments



class Quiz(db.Model):
    __tablename__ = 'quizes'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    category = db.Column(db.Integer)
    posted = db.Column(db.Time, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment = db.relationship('Comment',backref = 'quiz',lazy = "dynamic")

    def save_quiz(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_quiz(cls, id):
        quiz = Quiz.query.filter_by(id=id).first()
        return quiz

    @classmethod
    def get_quizes(cls, id):
        quizes = Quiz.query.filter_by(id=id).all()
        return quizes

    def delete_quiz(self):
        db.session.delete(self)
        db.session.commit()
