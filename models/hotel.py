from conexao import bd

class HotelModel(bd.Model):
    __tablename__ = "hoteis"
    hotel_id = bd.Column(bd.string, primary_key=True)
    nome = bd.Column(bd.string(80))
    estrelas = bd.Column(bd.Float(precision=1))
    diaria = bd.Column(bd.Float(precision=2))
    cidade = bd.Column(bd.string(80))

    def __init__(self):
        super().__init__()