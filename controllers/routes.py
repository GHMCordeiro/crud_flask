from flask import render_template, request, url_for, redirect
from models.database import db, Game
import urllib
import json

jogadores = []
jogos = []
gamelist = [{'Título' : 'CS-GO', 'Ano' : 2012, 'Categoria' : 'FPS Online'}]

def init_app(app):
    # Definindo a rota principal
    @app.route('/')
    # Função que será executada ao acessar a rota
    def home():
        # Retorno que será exibido na rota
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]
        
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
                
            if request.form.get('jogo'):
                jogos.append(request.form.get('jogo'))
                
        return render_template('games.html', game=game, jogadores=jogadores, jogos=jogos)
    
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título' : request.form.get('titulo'), 'Ano' : request.form.get('ano'), 'Categoria' : request.form.get('categoria')})
        return render_template('cadgames.html', gamelist=gamelist)
    
    @app.route('/apigames', methods=['GET', 'POST'])
    @app.route('/apigames/<int:id>', methods=['GET', 'POST'])
    def apigames(id=None):
        url = 'https://www.freetogame.com/api/games'
        res = urllib.request.urlopen(url)
        data = res.read()
        gamesjson = json.loads(data)

        if id:
            ginfo = []
            for g in gamesjson:
                if g['id'] == id:
                    ginfo = g
            if ginfo:
                return render_template('gamesinfo.html', ginfo=ginfo)
            else:
                return f'O Game com a ID {id} não foi encontrado!'
        else:
            return render_template('apigames.html', gamesjson=gamesjson)  

    @app.route('/search', methods=['GET', 'POST'])  
    def search():
        url = 'https://www.freetogame.com/api/games'
        res = urllib.request.urlopen(url)
        data = res.read()
        gamesjson = json.loads(data)

        if request.method == 'POST':
            if request.form.get('game'):
                game = request.form.get('game')
                gsearch = []
                for g in gamesjson:
                    if g['title'] == game:
                        gsearch = g
                
                if gsearch:
                    print(gsearch)
                    return render_template('search.html', gsearch = gsearch)
                else:
                    return "Nao foi encontrado"
    

    ## CRUD - Listagem de dados
    
    @app.route('/estoque', methods=['GET', 'POST'])
    @app.route('/estoque/<int:id>')
    def estoque(id=None):
        ## Excluindo um jogo
        if id:
            game = Game.query.get(id)
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque'))

        if request.method == 'POST':
            newgame = Game(request.form['titulo'], request.form['ano'], request.form['categoria'], request.form['plataforma'], request.form['preco'], request.form['quantidade'])
            db.session.add(newgame)
            db.session.commit()
            return redirect(url_for('estoque'))
        else:
            gamesestoque = Game.query.all()
            return render_template('estoque.html', gamesestoque = gamesestoque)
                    