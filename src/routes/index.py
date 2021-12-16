from . import routes
from flask import jsonify
import numpy

data = numpy.repeat({
  "symbol": "AAPL 1",
  "name": "Apple, Inc.",
  "price": 149.26,
  "change": 0.34,
}, 30)

@routes.route("/")
def index():
    response = jsonify(message=data.tolist())

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
