from . import routes
from flask import jsonify, request
import numpy
from datagen import generate_news_data

data = generate_news_data(20)

'''data = numpy.repeat({
  "title": "US stocks hover near record territory - API",
  "description": "US stocks are trading higher",
  "author": "CNN Business",
  "date": "October 27, 2021",
  "link":  "https://www.cnn.com/business/live-news/stock-market-news-102721/index.html",
}, 20)'''

@routes.route("/news")
def news():
    limit = int(    request.args.get("limit", 5))
    index = int(request.args.get("index", 0))
    message = data[index:index+limit]
    response = jsonify(message=message, total = len(data))

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

