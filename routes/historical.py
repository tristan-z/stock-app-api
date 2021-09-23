from . import routes

@routes.route("/app/volume")
def volume():
    return "volume"