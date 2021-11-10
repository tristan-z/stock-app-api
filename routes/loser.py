from . import routes
from flask import jsonify
import numpy

data = numpy.repeat({
  "symbol": "KO",
  "name": "Coca-Cola Co",
  "price": 56.49,
}, 4)

@routes.route("/loser")
def loser():
    response = jsonify(message=data.tolist())

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

