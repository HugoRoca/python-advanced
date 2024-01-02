from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Hello world 😬❤️"


@app.route("/api", methods=["GET"])
def api():
    return {"message": "from JSON"}


@app.route("/api/<id>", methods=["GET"])
def api_id(id):
    return {"message": f"from JSON {id}"}


if __name__ == "__main__":
    app.run(port=3000, debug=True)
