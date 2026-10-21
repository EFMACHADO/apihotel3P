from conexao import bd
class HotelModel(bd.Model):
    __tablename__ = "hoteis"
    hotel_id = bd.Column(bd.String, primary_key=True)
    nome = bd.Column(bd.String(80))
    estrelas = bd.Column(bd.Float(precision=1))
    diaria = bd.Column(bd.Float(precision=2))
    cidade = bd.Column(bd.String(80))
    
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        
    def json(self):
        return {
            "hotel_id": self.hotel_id,
            "nome": self.nome,
            "estrelas": self.estrelas,
            "diaria": self.diaria,
            "cidade": self.cidade
        }
        
    @classmethod
    def find_hotel(cls, id_hotel):
        hotel = cls.query.filter_by(hotel_id=id_hotel).first() 
        # SELECT * FROM hoteis WHERE hotel_id = id_hotel LIMIT 1
        if hotel:
            return hotel
        return None
    
    def save_hotel(self):
        bd.session.add(self)
        bd.session.commit()
        
    def delete_hotel(self):
        bd.session.delete(self)
        bd.session.commit()
        
    def update_hotel(self, nome, estrelas, diaria, cidade):
            self.nome = nome
            self.estrelas = estrelas
            self.diaria = diaria
            self.cidade = cidade