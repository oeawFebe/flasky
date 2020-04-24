from flask import Flask

app=Flask(__name__)

# @app.route("/")
# def index():
#     return "<h1>Hello World!</h1>"

from flask import request
@app.route("/")
def index():#request enables to access globally certain obj without adding an arg to view func
    user_agent=request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)