from flask import Flask, Blueprint
from flask_restplus import Api


class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint,
                    doc='/doc',
                    title='API',
                    version='1.0',
                    description='API'
                    )
        self.app.register_blueprint(self.blueprint)
        
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        
        self.book_ns = self.book_ns()
        
    def book_ns(self, ):
        return self.api.add_namespace(name='Books',
                                        description='boos related operations', path='/')

    def run(self, ):
        self.app.run(
            debug=True,
            port=5000,
            host='0.0.0.0'
            )
server = Server()
