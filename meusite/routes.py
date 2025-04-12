from flask import render_template, redirect, url_for, flash, request
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
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(
            f'Login realizado com sucesso. E-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('homepage'))
    else:
        flash(f'Falha no Login. E-mail ou Senha Incorretos', 'alert-danger')

    return render_template('login.html', form_login=form_login)


@app.route('/conta', methods=['GET', 'POST'])
def conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash(
            f'Conta criada com sucesso. E-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('homepage'))
    else:
        flash(f'Falha ao criar conta. E-mail ou Senha Incorretos', 'alert-danger')
    return render_template('conta.html', form_criarconta=form_criarconta)
