# formulário web
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[
                          DataRequired(), Length(min=6, max=20)])
    confirmacao_senha = PasswordField('Confirmação da senha', validators=[
                                DataRequired(), EqualTo('senha', message='As senhas devem ser iguais')])
    botao_submit_criarconta = SubmitField('Criar conta')


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[
                          DataRequired(), Length(min=6, max=20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')
