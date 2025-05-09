# No terminal, vamos obter um token
## python
## import secrets
## secrets.token_hex(16)
# Coloque o token no app.config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = '606cb54f74dfd605d7793bf6d3dfe38e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Isto serve para configurar onde entrar caso o login seja exigido
login_manager.login_view = 'login' 
login_manager.login_message_category = 'alert-info'
login_manager.login_message = 'Por favor, faça login para acessar esta funcionalidade.'

from meusite import routes



