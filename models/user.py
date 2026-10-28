from conexao import bd
class userModel(bd.Model):
    __tablename__ = "hoteis"
    user_id = bd.Column(bd.String, primary_key=True)
    nome = bd.Column(bd.String(80))
    estrelas = bd.Column(bd.Float(precision=1))
    diaria = bd.Column(bd.Float(precision=2))
    cidade = bd.Column(bd.String(80))
    
    def __init__(self, user_id, nome, estrelas, diaria, cidade):
        self.user_id = user_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        
    def json(self):
        return {
            "user_id": self.user_id,
            "nome": self.nome,
            "estrelas": self.estrelas,
            "diaria": self.diaria,
            "cidade": self.cidade
        }
        
    @classmethod
    def find_user(cls, id_user):
        user = cls.query.filter_by(user_id=id_user).first() 
        # SELECT * FROM hoteis WHERE user_id = id_user LIMIT 1
        if user:
            return user
        return None
    
    def save_user(self):
        bd.session.add(self)
        bd.session.commit()
        
    def delete_user(self):
        bd.session.delete(self)
        bd.session.commit()
        
    def update_user(self, nome, estrelas, diaria, cidade):
            self.nome = nome
            self.estrelas = estrelas
            self.diaria = diaria
            self.cidade = cidade