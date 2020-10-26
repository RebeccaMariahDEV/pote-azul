from flask import request
from flask_restful import Resource


class CreateClient(Resource):

    def post(self):
        # Salvar os dados recebidos no banco
        data = request.json
        return data, 200


class ClienteHandler(Resource):
    # Fazer funcionar com parametros recebidos
    def get(self, cliente_id):
        # Busca um item do banco, pelo seu id
        return f"id encontrado é o {cliente_id}", 200

    def delete(self, cliente_id):
        # Deleta um item do banco, pelo seu id
        return f"id encontrado é o {cliente_id}", 200

    def patch(self, cliente_id):
        # Atualiza um item do banco, pelo seu id
        data = request.json
        return f"id encontrado é o {cliente_id}", 200


class CreateList(Resource):

    def get(self):
        # Salvar os dados recebidos no banco
        data = request.json
        return "Finge que é uma lista", 200