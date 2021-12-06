from . import routes
from flask import jsonify
import numpy
from faker import Faker

fake = Faker()

def generate_data(n):
    data = []
    for _ in range(n):
      obj= {}
      obj["symbol"] = fake.name()
      obj["name"] = fake.text()
      obj["price"] = fake.pricetag()
      data.append(obj)
    return data

# data = numpy.repeat(generate_data(), 4)
data = generate_data(4)

@routes.route("/loser")
def loser():
    response = jsonify(message=data)

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

