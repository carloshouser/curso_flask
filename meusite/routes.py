from flask import render_template, url_for
from meusite import app

lista_usuarios = ['Marcio', 'Daniel', 'Alessandro', 'Carlos', 'Luíz']

@app.route('/')
def homepage():
    return render_template('home.html') 

@app.route('/contatos')
def contatos():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios = lista_usuarios)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/conta')
def conta():
    return render_template('conta.html')

