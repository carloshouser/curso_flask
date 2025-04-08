from meusite import app

@app.route('/')
def homepage():
    return 'Teste'

