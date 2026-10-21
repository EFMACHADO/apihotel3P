from flask import Flask;
from flask_restful import Resource, Api
from resources.hotel import Hoteis, Hotel
from conexao import bd
app = Flask(__name__)
# Configurações
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hoteis.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
# Rotas
api.add_resource(Hoteis,"/hoteis")
api.add_resource(Hotel,"/hoteis/<string:id_hotel>")
# Iniciar a aplicação
if __name__ == "__main__":
    bd.init_app(app)
    with app.app_context():
        bd.create_all()
    app.run(debug=True)