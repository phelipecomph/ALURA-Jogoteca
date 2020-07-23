from flask import Flask, render_template, request

app = Flask(__name__)
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

lista = [Jogo("Super Mario", 'Aventura', 'SNES'),
             Jogo('Super Fire', 'RPG', 'GBA')]

@app.route('/') #GET
def index():
    return render_template('lista.html', titulo="Jogos",
                                        jogos=lista)

@app.route('/novo') #GET
def novo():
    return render_template('novo.html', titulo="Novo Jogo")

@app.route('/criar', methods=['POST']) #POST
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo="Jogos",
                                        jogos=lista)

app.run(host='127.0.0.1', port=8000)#, debug=True)                                                        