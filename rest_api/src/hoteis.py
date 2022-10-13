from flask_restful import Resource, reqparse

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
    def get(self, id):
        for hotel in hoteis_bd:
            if hotel['id'] == id:
                return hotel
        return {'message': 'Hotel not found.'}, 404
        
    
    def post(self, id):
        arg_list = reqparse.RequestParser()
        arg_list.add_argument('nome'),
        arg_list.add_argument('estrelas'),
        arg_list.add_argument('diaria'),
        arg_list.add_argument('cidade'),
        
        new_args = arg_list.parse_args()
        
        new_hotel = {
            'id': id,
            'nome': new_args['nome'],
            'estrelas': new_args['estrelas'],
            'diaria': new_args['diaria'],
            'cidade': new_args['cidade']
        }
        
        hoteis_bd.append(new_hotel)
        
        return new_hotel, 200
        
    
    def put(self):
        pass
    
    def delete(self):
        pass
    