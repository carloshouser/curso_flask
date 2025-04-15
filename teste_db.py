from meusite import app, database
from meusite.models import Usuario, Post


# with app.app_context():
#     database.drop_all()
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username = 'Carlos', email = 'carlos.pereira@cds.com', senha='123456')
#     usuario2 = Usuario(username = 'Luiz', email = 'luiz@cds.com', senha='123123')
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()

# with app.app_context():
#     # meus_usuarios = Usuario.query.all()
#     meus_usuarios = Usuario.query.first()
#     print(meus_usuarios.id)
#     print(meus_usuarios.email)
#     print(meus_usuarios.posts)

# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(id=2).first()
#     print(usuario_teste.email)

# with app.app_context():
#     meu_post = Post(id_usuario = 1, titulo = 'Meu Primeiro Post' , corpo ='Teste' , )
#     database.session.add(meu_post)
#     database.session.commit()

# with app.app_context():
#     meu_post = Usuario.query.filter_by(id=1).first()
#     print(meu_post.username)
#     print(meu_post.posts[0].titulo)

# with app.app_context():
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.autor.email)

# with app.app_context():
#     usuario = Usuario.query.first()
#     print(usuario.senha)
