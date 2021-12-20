from . import routes
from flask import jsonify
import numpy

# TODO: abstract response construction to utilities 

message = "the api is running"

@routes.route("/")
def index():
    response = jsonify(message=message)

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
