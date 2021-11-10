from . import routes
from flask import jsonify
import numpy

data = numpy.repeat({
  "stock": "TSLA"
}, 4)

@routes.route("/gainer")
def gainer():
    response = jsonify(message=data.tolist())

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

