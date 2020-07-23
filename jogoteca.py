from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'ph' #secrect key necessario para utilizar o session

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
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', titulo="Login")

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['senha'] == 'mestra':
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' Logou com sucesso!')
        return redirect('/')
    else:
        flash('Não logado, tente novamente')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuario deslogado')
    return redirect('/')

app.run(host='127.0.0.1', port=8000, debug=True)                                                        