# Para criar o banco de dados:
# no terminal do python:
# from meusite import database
# with app_context:
# database.create_all()

from flask import render_template, redirect, url_for, flash, request
from meusite import app, database, bcrypt
from meusite.forms import FormCriarConta, FormLogin, FormEditarPerfil
from meusite.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required

lista_usuarios = ['Marcio', 'Daniel', 'Alessandro', 'Carlos', 'Luíz']


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/contatos')
def contatos():
    return render_template('contato.html')


@app.route('/usuarios')
@login_required
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(
                f'Login realizado com sucesso. E-mail: {form_login.email.data}', 'alert-success')
            parametro_next = request.args.get('next')
            if parametro_next:
                return redirect(parametro_next)
            else:
                return redirect(url_for('homepage'))
        else:
            flash(
                f'Falha no login. E-mail ou senha incorretos.', 'alert-danger')
    return render_template('login.html', form_login=form_login)


@app.route('/conta', methods=['GET', 'POST'])
def conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data,
                          email=form_criarconta.email.data,
                          senha=senha_cript)

        database.session.add(usuario)
        database.session.commit()

        flash(
            f'Conta criada com sucesso. E-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('homepage'))
    else:
        flash(f'Falha ao criar conta. E-mail ou Senha Incorretos', 'alert-danger')
    return render_template('conta.html', form_criarconta=form_criarconta)


@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash(f'Logout feito com sucesso!', 'alert-success')
    return redirect(url_for('homepage'))


@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    #foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('perfil.html', foto_perfil=foto_perfil)


@app.route('/post/criacao')
@login_required
def criar_post():
    return render_template('criarpost.html')

@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form = FormEditarPerfil()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    return render_template('editar_perfil.html', foto_perfil=foto_perfil, form=form)
