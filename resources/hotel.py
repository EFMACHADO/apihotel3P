from flask_restful import Resource, reqparse

lista_hoteis = [
    { "hotel_id": "sky", "nome": "Hotel Sky", "estrelas": 4.8, "diaria": 195.99, "cidade": "Porto"},
    { "hotel_id": "paraiso", "nome": "Paraiso Resort", "estrelas": 4.9, "diaria": 299.99, "cidade": "Lisboa"},
    { "hotel_id": "water", "nome": "Hotel Water", "estrelas": 4.5, "diaria": 175.99, "cidade": "Famalicão"}
]

class Hoteis(Resource):
    def get(self):
        return { "hoteis": lista_hoteis }

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, required=True, help="Nome obrigatório")
    argumentos.add_argument("estrelas", type=float, required=True, help="Estrelas obrigatório")
    argumentos.add_argument("diaria", type=float, required=True, help="Diária obrigatório")
    argumentos.add_argument("cidade", type=str, required=True, help="Cidade obrigatório")
   
    def get(self, id_hotel):
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == id_hotel:
                return hotel, 200
        return { "message": "Hotel not found" }, 404
   
    def post(self,id_hotel):
        dados = Hotel.argumentos.parse_args() # Dicionário
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == id_hotel:
                return { "message": "Hotel with this id already exists"}
        novo_hotel = { "hotel_id": id_hotel, **dados }
        lista_hoteis.append(novo_hotel)
        return novo_hotel, 200
   
    def put(self,id_hotel):
        dados = Hotel.argumentos.parse_args() # Dicionário
        for hotel in lista_hoteis:
            if hotel["hotel_id"] == id_hotel:
                hotel.update(**dados)
                return hotel, 200
        novo_hotel = { "hotel_id": id_hotel, **dados }
        lista_hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, id_hotel):
        global lista_hoteis
        lista_hoteis = [hotel for hotel in lista_hoteis if hotel["hotel_id"] != id_hotel]
        return {"message": "Hotel deleted"}