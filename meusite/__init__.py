# No terminal, vamos obter um token
## python
## import secrets
## secrets.token_hex(16)
# Coloque o token no app.config

from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '606cb54f74dfd605d7793bf6d3dfe38e'

from meusite import routes



