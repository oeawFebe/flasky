import os
from app import create_db,db
from app.models import User,Role
from flask_migrate import Migrate

app=create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate=Migrate(app,db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User,Role=Role)





from flask import Flask,render_template,flash,session,redirect,url_for,request


# @app.route("/")
# def index():
#     return "<h1>Hello World!</h1>"

# @app.route("/",methods=["GET","POST"])
# def index():#request enables to access globally certain obj without adding an arg to view func
#     form=NameForm()
#     if form.validate_on_submit():
#         user=User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             user=User(username=form.name.data)
#             db.session.add(user)
#             db.session.commit()
#             session['known']=False
#             if app.config['FLASKY_ADMIN']:
#                 send_email(app.config['FLASKY_ADMIN'],'New User','mail/new_user',user=user)
#         else:
#             session['known']=True
#         session['name']=form.name.data
#         form.name.data=""
#         return redirect(url_for('index'))
#     return render_template('index.html',form=form,name=session.get('name'),known=session.get('known',False))
    #current_time=datetime.utcnow()

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
