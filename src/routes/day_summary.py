from . import routes
from flask import jsonify
import numpy
from faker import Faker
import random

fake = Faker()

def generate_data(n):
    data = []
    for _ in range(n):
      obj= {}
      obj["symbol"] = fake.name()
      obj["name"] = fake.company()
      obj["price"] = round(random.uniform(0, 10000), 2)
      obj["change"] = round(random.uniform(-100, 100), 2)
      data.append(obj)
    return data

data = generate_data(30)

@routes.route("/day-summary")
def day_summary():
    response = jsonify(message=data)

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
