from flask_restful import Api

from cliente.handler import ClienteHandler, CreateClient, CreateList


def set_urls(app):
    api = Api()
    api.add_resource(CreateClient, "/cliente")
    api.add_resource(ClienteHandler, "/cliente/<cliente_id>")
    api.add_resource(CreateList, "/cliente/all")
    api.init_app(app)
