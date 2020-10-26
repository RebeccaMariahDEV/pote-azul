from flask import request
from flask_restful import Resource


class ClienteHandler(Resource):

    def get(self):
        # Busca um item do banco, pelo seu id
        return f"id encontrado é o", 200

    def post(self):
        # Salvar os dados recebidos no banco
        data = request.json
        return {}, 200

    def delete(self, id):
        # Deleta um item do banco, pelo seu id
        return {}, 200

    def patch(self, id):
        # Atualiza um item do banco, pelo seu id
        data = request.json
        return {}, 200
