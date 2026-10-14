from flask_restful import Resource

lista_hoteis = [
     { "hotel_id": "sky", "nome": "Hotel Sky", "estrelas": 5, "diaria": 599.99, "cidade": "Porto"},
     { "hotel_id": "sky", "nome": "Hotel Situações", "estrelas": 5, "diaria": 412.72, "cidade": "Lisboa"},
     { "hotel_id": "sky", "nome": "Hotel Febras", "estrelas": 2, "diaria": 176.21, "cidade": "Troia"}
]

class Hoteis(Resource):
    def get(self):
        return { "hoteis": lista_hoteis }
