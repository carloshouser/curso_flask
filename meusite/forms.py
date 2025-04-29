# formulário web
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from meusite.models import Usuario


class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[
                          DataRequired(), Length(min=6, max=20)])
    confirmacao_senha = PasswordField('Confirmação da senha', validators=[
        DataRequired(), Length(min=6, max=20), EqualTo('senha', message='As senhas devem ser iguais')])
    botao_submit_criarconta = SubmitField('Criar conta')

    # A função do Flask validate_on_submit(), que está sendo usada lá no routes
    # verifica todas as validações definida no forms e também roda todas as funções
    # que começam com "validate_"
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Este e-mail já foi cadastrado. Cadastre-se com outro e-mail ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=20)])    
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    botao_submit_editarperfil = SubmitField('Confirmar Edição')
