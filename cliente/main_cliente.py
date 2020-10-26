from flask import Flask, request

from cliente.urls_cliente import set_urls

app = Flask(__name__)
set_urls(app)


if __name__ == "__main__":
    app.run()
