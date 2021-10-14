from . import routes

@routes.route("/")
def index():
    return "api active"