from flask_restful import Resource, reqparse
from models.hotel import HotelModel
class Hoteis(Resource):
    def get(self):
        return { "hoteis": [hotel.json() for hotel in HotelModel.query.all()] }
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, required=True, help="Nome obrigatório")
    argumentos.add_argument("estrelas", type=float, required=True, help="Estrelas obrigatórias")
    argumentos.add_argument("diaria", type=float, required=True, help="Diaria obrigatória")
    argumentos.add_argument("cidade", type=str, required=True, help="Cidade obrigatória")
    
    def get(self, id_hotel):
        hotel = HotelModel.find_hotel(id_hotel)
        if hotel:
            return hotel.json(), 200
        return {"message": "Hotel not found"}, 404 # NOT FOUND
    def post(self, id_hotel):
        dados = Hotel.argumentos.parse_args() # Dicionário
        hotel = HotelModel.find_hotel(id_hotel)
        if hotel:
            return { "message": "Hotel with this id already exists"}
        
        try:
            novo_hotel = HotelModel(id_hotel, **dados)
            novo_hotel.save_hotel()
            return novo_hotel.json(), 200 # CREATED
        except:
            return { "message": "Internal error ..."}, 500 # INTERNAL ERROR
    def put(self, id_hotel):
        dados = Hotel.argumentos.parse_args() # Dicionário
        hotel = HotelModel.find_hotel(id_hotel)
        if hotel:
            try:
                hotel.update_hotel(dados["nome"],dados["estrelas"],dados["diaria"],["cidade"])
                hotel.save_hotel()
                return hotel.json(), 200 # UPDATED
            except:
                return { "message": "Internal error ..."}, 500 # INTERNAL ERROR
            
        try:
            novo_hotel = HotelModel(id_hotel, **dados)
            novo_hotel.save_hotel()
            return novo_hotel.json(), 201 # CREATED
        except:
            return { "message": "Internal error ..."}, 500 # INTERNAL ERROR
     
    def delete(self, id_hotel):
        hotel = HotelModel.find_hotel(id_hotel)
        if hotel:
            try:
                hotel.delete_hotel()
                return {"message": "Hotel deleted"}, 200 # DELETED
            except:
                return { "message": "Internal error ..."}, 500 # INTERNAL ERROR
        return {"message": "Hotel not found"}, 404 # NOT FOUND