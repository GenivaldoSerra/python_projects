from flask import Flask, Blueprint
from flask_restplus import Api


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint,
                    doc='/doc',
                    title='API',
                    version='1.0',
                    description='API'
                    )
        self.app.register_blueprint(self.blueprint)

    def run(self):
        self.app.run(debug=True)