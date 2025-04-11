from flask import render_template, url_for
from meusite import app
from meusite.forms import FormCriarConta, FormLogin

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
    form_login = FormLogin()
    return render_template('login.html', form_login=form_login)

@app.route('/conta')
def conta():
    form_criarconta = FormCriarConta()
    return render_template('conta.html', form_criarconta=form_criarconta)

