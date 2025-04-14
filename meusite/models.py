from meusite import database, login_manager
from datetime import datetime, timezone

# Este UserMixin é um parâmetro que vamos passar para a classe
#  que irá atribuir para esta classe todas as características que
#  o LoginManager precisa para controlar os logins, por exemplo,
#  deslogar, master o usuário conectado, lembrar do login.
from flask_login import UserMixin 

# Libera logins no sistema. Esta função tem o propósito de 
# buscar um usuário  no sistema
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))



class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg', nullable=False)
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não Informado')


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    # data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.now(timezone.utc))
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    
