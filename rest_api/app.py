from flask import Flask
from flask_restful import Api

from resources.hoteis import Hoteis, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_data():
    data.create_all()

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:id>')

if __name__ == '__main__':
    from sql_alchemy import data
    data.init_app(app)
    app.run(debug=True)