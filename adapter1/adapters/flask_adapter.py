from flask import Flask, request, jsonify
from app.business_logic import get_hello
from adapters.base import AppAdapter


class FlaskAdapter(AppAdapter):
    def __init__(self):
        self.app = Flask(__name__)
        self._setup_routes()

    def _setup_routes(self):
        @self.app.route("/hello", methods=["GET"])
        def hello():
            name = request.args.get("name", "World")
            return jsonify(get_hello(name))

    def run(self):
        self.app.run(debug=True)
