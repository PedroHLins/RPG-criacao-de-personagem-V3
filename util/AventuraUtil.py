from .DadoUtil import Dado

class Aventura:

    @staticmethod
    def rolar_valores_3d6():
        valores_disponiveis = []
        for i in range(6):
            resultado = sum(Dado.rolar3d6())
            valores_disponiveis.append(resultado)
        return valores_disponiveis

    @staticmethod
    def classico_aventureiro():
        return Aventura.rolar_valores_3d6()

    @staticmethod
    def heroico():
        valores_disponiveis = []
        for i in range(6):
            dados_list = Dado.rolar4d6()
            dado_menor = min(dados_list)
            dados_list.remove(dado_menor)
            resultado = sum(dados_list)
            valores_disponiveis.append(resultado)
        return valores_disponiveis