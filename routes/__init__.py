from flask import Blueprint
routes = Blueprint('routes', __name__)

from .historical import *

from .index import *