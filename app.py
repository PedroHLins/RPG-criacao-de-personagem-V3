from flask import Flask, render_template, request

from services.PersonagemService import PersonagemService
from util.AventuraUtil import Aventura
from util.DistribuicaoUtil import Distribuicao

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template("index.html")

@app.route("/Criar-Persongaem", methods=["POST"])
def criar_novo_personagem():
    service = PersonagemService()
    personagem = service.criar_persongaem_inicial(request.form)
    tipo_aventura = request.form["aventura"]

    if tipo_aventura == "Classica":
        valores = Aventura.classico_aventureiro()
        Distribuicao.classico(personagem, valores)
        return render_template("ficha.html", personagem=personagem)
    elif tipo_aventura == "Aventureira":
        valores = Aventura.classico_aventureiro()
    else:
        valores = Aventura.heroico()

    return render_template("distribuicao.html", personagem=personagem, valores=valores)

@app.route("/Ficha", methods=["POST"])
def exibir_ficha():
    personagem_service = PersonagemService()
    personagem_final = personagem_service.criar_persongaem_final(request.form)
    return render_template("ficha.html", personagem=personagem_final)

if __name__ == "__main__":
    app.run(debug = True)