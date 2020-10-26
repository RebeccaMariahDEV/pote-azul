from flask_restful import Api

from cliente.handler import ClienteHandler


def set_urls(app):
    api = Api()
    api.add_resource(ClienteHandler, "/cliente")
    api.init_app(app)
