from flask import Blueprint
main=Blueprint('main',__name__)#the blueprintname, its location(the module/package name)
from . import views,errors
