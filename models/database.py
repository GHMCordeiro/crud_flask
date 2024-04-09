from flask_sqlalchemy import SQLAlchemy

## Carrega o SQLAlchemy ##
db = SQLAlchemy()

## Classe responsável por criar a entidade Games com seus atributos ##
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)

    def __init__(self, titulo, ano, categoria, plataforma, preco, quantidade):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade

## Classe responsável por criar a entidade Usuário no banco
        
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password