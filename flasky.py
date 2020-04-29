import os

COV=None
if os.environ.get("FLASK_COVERAGE"):
    import coverage
    COV=coverage.coverage(branch=True,include="app/*")
    COV.start()

import sys,click
from app import create_app,db
from app.models import User,Role,Follow,Permission,Post,Comment
from flask_migrate import Migrate


app=create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate=Migrate(app,db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User,Role=Role,Follow=Follow,
        Permission=Permission,Post=Post,Comment=Comment)


# @app.cli.command()
# def test():
#     """Run the unittest. """
#     import unittest
#     tests=unittest.TestLoader().discover("tests")
#     unittest.TextTestRunner(verbosity=2).run(tests)

@app.cli.command()
@click.option("--coverage/--no-coverage",default=False,help="Run tests under code coverage.")
@click.argument("test_names",nargs=-1)
def test(coverage,test_names):
    """Run the unit tests."""
    if coverage and not os.environ.get("FLASK_COVERAGE"):
        import subprocess
        os.environ["FLASK_COVERAGE"]="1"
        sys.exit(subprocess.call(sys.argv))
    import unittest
    if test_names:

        tests=unittest.TestLoader().loadTestsFromNames(test_names)
    else:

        tests=unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print("Coverage Summary:")
        COV.report()
        basedir=os.path.abspath(os.path.dirname(__file__))
        covdir=os.path.join(basedir,"temp/coverage")
        COV.html_report(directory=covdir)
        print("HTML version: file://%s/index.html" % covdir)
        COV.erase()
#################################################################

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

