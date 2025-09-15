from flask import Flask, render_template, request

from services.PersonagemService import PersonagemService

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template("index.html")

@app.route("/Criar-Persongaem", methods=["POST"])
def criar_novo_personagem():
    service = PersonagemService()
    personagem = service.criar_persongaem(request.form)
    return render_template("ficha.html", personagem=personagem)

if __name__ == "__main__":
    app.run(debug = True)