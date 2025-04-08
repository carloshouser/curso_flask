from flask import render_template
from meusite import app

@app.route('/')
def homepage():
    return render_template('home.html') 

@app.route('/contatos')
def contatos():
    return render_template('contato.html')

