from flask import Flask 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#Configurações 

#Rotas

#Iniciar a Aplicação
if __name__=="__main__":
    app.run(debug=True)