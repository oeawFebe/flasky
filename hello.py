from flask import Flask,render_template,flash,session,redirect,url_for,request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail,Message
from datetime import datetime
from threading import Thread

app=Flask(__name__)

migrate=Migrate(app,db)


class NameForm(FlaskForm):
    name=StringField('What is your name?', validators=[DataRequired()])#it isan html input elem with type="text"
    submit=SubmitField('Submit')#it is basically an html input elem with type="submit" attr

class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    users=db.relationship('User',backref='role',lazy='dynamic')
    def __repr__(self):
        return '<Role %r>' % self.name
class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username

def send_email(to,subject,template,**kwargs):#kwargs will be template context, see line 3,4 below
    msg=Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject,sender=app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    
    msg.body=render_template(template+'.txt',**kwargs)
    msg.html=render_template(template+'.html',**kwargs)
    thr=Thread(target=send_async_email,args=[app,msg])
    thr.start()
    return thr    
def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)
# @app.route("/")
# def index():
#     return "<h1>Hello World!</h1>"


# @app.route("/")
# def index():
#     return '<h1>Bad Request</h1>',400
# from flask import make_response

# @app.route("/")
# def index():
#     response=make_response("<h1>This document carries a cookies!</h1>")
#     response.set_cookie('answer','42')
#     return response

# @app.route("/")
# def index():
#     return redirect("http://www.example.com")

# from flask import abort
# @app.route("/user/<id>")
# def get_user(id):
#     user=load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello, {}</h1>'.format(user.name)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html",name=name)
@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User,Role=Role)

