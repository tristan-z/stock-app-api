from . import routes
from flask import jsonify


@routes.route("/")
def index():
    response = jsonify("Api Active")

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
