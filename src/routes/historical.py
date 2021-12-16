from . import routes
from flask import jsonify

@routes.route("/app/volume")
def volume():
    return {
        "data":
 {
   "Date": "09/08/2021",
   "Close": {
      "Last": "$155.11"
   },
   "Volume": 74420210,
   "Open": "$156.98",
   "High": "$157.04",
   "Low": "$153.975"
},
    }