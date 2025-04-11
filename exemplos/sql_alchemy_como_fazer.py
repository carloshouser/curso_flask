# create_engine serve para criar o banco de dados
from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base


db = create_engine('sqlite:///meubanco.db')

Session = sessionmaker(bind=db)
session=Session()

Base = declarative_base()

# as tabelas
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    email = Column('email', String)
    senha = Column('senha', String)
    ativo = Column('ativo', Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email=email
        self.senha=senha
        self.ativo=ativo


class Livro(Base):
    __tablename__ = 'livros'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    titulo = Column('titulo', String)
    qtde_paginas = Column('qtde_paginas', Integer)
    dono = Column('dono', ForeignKey('usuarios.id'))

    def __init__(self, titulo, qtde_paginas, dono):        
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono

Base.metadata.create_all(bind=db)

# CRUD

##### C- Create #####
# usuario = Usuario(nome='Carlos', email='teste@gmail.com', senha='123123')
# session.add(usuario)
# session.commit()

# usuario = Usuario(nome='Carloss', email='testes@gmail.com', senha='123321')
# session.add(usuario)
# session.commit()

##### R- READ #####
# lista_usuarios = session.query(Usuario).all()
# um_usuario = lista_usuarios = session.query(Usuario).first()

# Isto retorna uma query, um select propriamente dito
# usuario_carlos = session.query(Usuario).filter_by(email='teste@gmail.com')

# Isto restorna um objeto
# usuario_carlos = session.query(Usuario).filter_by(email='teste@gmail.com').first()

# Isto restorna uma lista de objetos
# usuario_carlos = session.query(Usuario).filter_by(email='teste@gmail.com').all()

# Acessando as informações do objeto
# usuario_carlos = session.query(Usuario).filter_by(email='teste@gmail.com').first()
# print(usuario_carlos.nome, usuario_carlos.email)

# livro = Livro(titulo='Nome do Vento', qtde_paginas=1000, dono=usuario_carlos.id)
# session.add(livro)
# session.commit()

##### U- UPDATE #####
# usuario_carlos = session.query(Usuario).filter_by(email='teste@gmail.com').first()
# usuario_carlos.nome = 'Carlos Alberto'
# session.add(usuario_carlos)
# session.commit()

##### DELETE #####
# carlos2 = session.query(Usuario).filter_by(email='testes@gmail.com').first()
# session.delete(carlos2)
# session.commit()
