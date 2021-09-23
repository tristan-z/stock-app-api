from . import routes

@routes.route("/")
def main():
    return "api active"