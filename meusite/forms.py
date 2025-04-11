# formulário web
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[
                          DataRequired(), Length(min=6, max=20)])
    confirmacao = PasswordField('Confirmação da senha', validators=[
                                DataRequired(), EqualTo('senha', message='As senhas devem ser iguais')])
    botao_submit = SubmitField('Criar conta')


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[
                          DataRequired(), Length(min=6, max=20)])
    botao_submit = SubmitField('Fazer Login')
