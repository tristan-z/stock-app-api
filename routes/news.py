from . import routes
from flask import jsonify
import numpy

data = numpy.repeat({
  "title": "US stocks hover near record territory - API",
  "description": "US stocks are trading higher",
  "author": "CNN Business",
  "date": "October 27, 2021",
  "link":  "https://www.cnn.com/business/live-news/stock-market-news-102721/index.html",
}, 4)

@routes.route("/news")
def news():
    response = jsonify(message=data.tolist())

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

