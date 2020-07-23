from flask import Flask, render_template

app = Flask(__name__)
    class Jogo:
        def __init__(self, nome, categoria, console):
            self.nome = nome
            self.categoria = categoria
            self.console = console

@app.route('/inicio')
def ola():

    lista = [Jogo("Super Mario", 'Aventura', 'SNES'),
             Jogo('Super Fire', 'RPG', 'GBA')]
    return render_template('lista.html', titulo="Jogos",
                                        jogos=lista)

app.run(host='127.0.0.1', port=8000)                                                        