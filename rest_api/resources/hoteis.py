from flask_restful import Resource, reqparse

from model.hotel import HotelModel

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
    arg_list = reqparse.RequestParser()
    arg_list.add_argument('nome'),
    arg_list.add_argument('estrelas'),
    arg_list.add_argument('diaria'),
    arg_list.add_argument('cidade'),
    
    def find_hotel(self, id):
        for hotel in hoteis_bd:
            if hotel['id'] == id:
                return hotel
        return None
    def get(self, id):
        hotel = self.find_hotel(id)
        if hotel:
            return hotel
        return {'message': 'Hotel not found.'}, 404
        
    
    def post(self, id):
        new_args = self.arg_list.parse_args()
        hotel_obj = HotelModel(id, **new_args)
        new_hotel = hotel_obj.json()
        hoteis_bd.append(new_hotel)
        
        return new_hotel, 201
        
    
    def put(self, id):
        dados = self.arg_list.parse_args()
        hotel_obj = HotelModel(id, **dados)
        new_hotel = hotel_obj.json()
        hotel = self.find_hotel(id)
        if hotel:
            hotel.update(new_hotel)
            return new_hotel, 200
        hoteis_bd.append(new_hotel)
        return new_hotel, 201
    
    
    def delete(self, id):
        global hoteis_bd
        hoteis_bd = [hotel for hotel in hoteis_bd if hotel['id'] != id]
        return {'message': 'Hotel deleted.'}, 200
    