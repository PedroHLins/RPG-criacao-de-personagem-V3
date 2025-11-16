import json
import os

from models.Personagem import Personagem
from models.classes.Gurreiro import Guerreiro
from models.classes.Ladrao import Ladrao
from models.classes.Mago import Mago
from models.racas.Anao import Anao
from models.racas.Elfo import Elfo
from models.racas.Halfling import Halfling
from models.racas.Humano import Humano
from util.DistribuicaoUtil import Distribuicao


class PersonagemService:
    def escolher_raca(self, raca):
        match raca:
            case "Humano":
                return Humano()
            case "Anao":
                return Anao()
            case "Elfo":
                return Elfo()
            case "Halfling":
                return Halfling()
        return None


    def escolher_classe(self, classe):
        match classe:
            case "Guerreiro":
                return Guerreiro()
            case "Mago":
                return Mago()
            case "Ladrao":
                return Ladrao()
        return None

    def criar_persongaem_inicial(self, dados_formulario):
        raca = self.escolher_raca(dados_formulario.get("raca"))
        classe = self.escolher_classe(dados_formulario.get("classe"))
        novo_personagem = Personagem(dados_formulario.get("char-name"), raca, classe)
        return novo_personagem

    def criar_persongaem_final(self, dados_formulario):
        personagem = self.criar_persongaem_inicial(dados_formulario)
        Distribuicao.aventureiro_heroico(personagem, dados_formulario)
        return personagem

    def salvar_personagem_json(self, personagem_final):

        dados_personagem = personagem_final.__dict__.copy()
        try:
            if hasattr(personagem_final.raca, "__dict__"):
                dados_personagem["raca"] = personagem_final.raca.__dict__

            if hasattr(personagem_final.classe, "__dict__"):
                dados_personagem["classe"] = personagem_final.classe.__dict__

            diretorio_service = os.path.abspath(os.path.dirname(__file__))
            diretorio_raiz = os.path.dirname(diretorio_service)
            diretorio_data = os.path.join(diretorio_raiz, "data")

            arq = os.path.join(diretorio_data, "ficha_personagens.json")

            with open(arq, "w", encoding="utf-8") as json_f:
                json.dump(dados_personagem, json_f, ensure_ascii=False, indent=4)

        except Exception as e:
            print(f"ERRO: {e}")