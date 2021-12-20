from flask import Blueprint
routes = Blueprint('routes', __name__)

from .index import *
from .historical import *
from .news import *
from .loser import *
from .gainer import *
from .day_summary import *