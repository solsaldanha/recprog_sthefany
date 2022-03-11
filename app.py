from config.Config import Config
from config.Database import Database
from dao.DiretorDao import DiretorDao
from flask import Flask, request, render_template

from model.Diretor import Diretor, Diretor

app = Flask(__name__)

dao = DiretorDao(Database(Config().config).conn)

@app.route('/', methods=["GET"])
def iniciar():
       return render_template(
        "main.html"
    )

@app.route('/diretor/novo', methods=["GET", "POST"])
def novo():
    diretor = Diretor
    return render_template("inserir.html")

@app.route('/diretor', methods=["POST"])
def inserir():
    diretor = Diretor()
    diretor.nome = request.form.get("nome")
    diretor.email = request.form.get("email")
    diretor.num_alunos = int(request.form.get("num_alunos"))
    diretor.idade = int(request.form.get("idade")) 

    dao.inserirDiretor(diretor)

    lista = dao.selecionarDiretores()
    return render_template(
        "listagem.html",
        lista=lista
    )

@app.route('/diretor', methods=["GET"])
def listar():
    lista = dao.selecionarDiretores()
    return render_template(
        "listagem.html",
        lista=lista
    )

@app.route('/diretor/<pid>', methods=["GET"])
def editarPagina(pid):
    diretor = dao.selecionarDiretor(pid)
    return render_template("editar.html", diretor= diretor)

@app.route('/diretor/editar', methods=["POST"])
def editar():

    diretor = Diretor()
    diretor.pid = request.form.get("pid")
    diretor.nome = request.form.get("nome")
    diretor.email = request.form.get("email")
    diretor.num_alunos = int(request.form.get("num_alunos"))
    diretor.idade = int(request.form.get("idade")) 
    diretor = dao.alterarDiretor(diretor)
    
    lista = dao.selecionarDiretores()
    return render_template(
        "listagem.html",
        lista=lista
    )

@app.route('/diretor/remover/<pid>', methods=["GET"])
def remover(pid):
    diretor = Diretor()
    diretor.pid = pid
    dao.excluirDiretor(diretor)
    
    lista = dao.selecionarDiretores()
    return render_template(
        "listagem.html",
        lista=lista
    )


if __name__ == '__main__':
    app.run()