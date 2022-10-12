from flask_restful import Resource


hoteis_bd = [
    {'id': 'alpha', 'nome': 'Alpha Hotel', 'estrelas': 4.3, 'diaria': 420.34, 'cidade': 'Rio de Janeiro'},
    {'id': 'bravo', 'nome': 'Bravo Hotel', 'estrelas': 4.4, 'diaria': 380.90, 'cidade': 'Santa Catarina'},
    {'id': 'charlie', 'nome': 'Charlie Hotel', 'estrelas': 4.1, 'diaria': 320.20, 'cidade': 'Santa Catarina'},
    {'id': 'delta', 'nome': 'Delta Hotel', 'estrelas': 3.9, 'diaria': 240.12, 'cidade': 'Minas Gerais'},
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis_bd}
    
class Hotel(Resource):
    def get(self):
        pass
    
    def post(self):
        pass
    
    def put(self):
        pass
    
    def delete(self):
        pass
    