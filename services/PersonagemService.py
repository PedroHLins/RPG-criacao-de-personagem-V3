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