    # Importando o Flask na aplicação
from flask import Flask, render_template
from controllers import routes
import os
from models.database import db

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

# Iniciando a função de rotas init_app passando o Flask como parâmetro
routes.init_app(app)

# Permitir ler o diretório absoluto de um determinado arquivo #
dir = os.path.abspath(os.path.dirname(__file__))

# Passando o diretório para o SQLAlchemy #
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/games.sqlite3')

# Definindo a secret_key para as flash messages
app.config['SECRET_KEY'] = 'thegamessecret'

# Define o tempo da sessão
app.config['PERMANENT_SESSION_LIFETIME'] = 1800

# Define a pasta uploads
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Define o tamanho mazximo de um arquivo de upload
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Se for executado diretamente pelo interpretador (arquivo principal)
if __name__ == '__main__': 
    # Verifica se o banco já existe, caso contrário, ele criará #
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    # Rodando a aplicação no localhost, porta 5000, modo debug ativado
    app.run(host='localhost', port=5001, debug=True)
