from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
app=Flask(__name__)
bootstrap=Bootstrap(app)
moment=Moment(app)
# @app.route("/")
# def index():
#     return "<h1>Hello World!</h1>"

from flask import request
@app.route("/")
def index():#request enables to access globally certain obj without adding an arg to view func
    return render_template('index.html',current_time=datetime.utcnow())

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