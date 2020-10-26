from flask import Flask, request

from cliente.urls_cliente import set_urls
from settings import DB_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
set_urls(app)


if __name__ == "__main__":
    app.run()
