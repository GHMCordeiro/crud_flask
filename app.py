# Importando o Flask na aplicação
from flask import Flask, render_template
from controllers import routes
import os
from models.database import db

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

# Iniciando a função de rotas init_app passando o Flask como parâmetro
routes.init_app(app)

# Permite ler o diretório absoluto de um determinado arquivo
dir = os.path.abspath(os.path.dirname(__file__))

# Passando o diretório para o SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/games.sqlite3')

# Se for executado diretamente pelo interpretador (arquivo principal)
if __name__ == '__main__': 
    # Verifica no início da aplicação se o BD já existe. Caso contrário ele criará o BD.
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    # Rodando a aplicação no localhost, porta 5000, modo debug ativado
    app.run(host='localhost', port=5000, debug=True)
