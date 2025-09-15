from models.classes.Classe import Classe

class Guerreiro(Classe):
    def __init__(self):
        super().__init__("Guerreiro", 10, 1)
        self.armas = ["Todas"]
        self.armaduras = ["Todas"]
        self.itens_magicos = ["Pergaminho de protecao"]
        # habilidade : nível necessário para usar habilidade
        self.habilidades = {"Maestria em arma" : 1, "Aparar" : 1, "Ataque extra" : 6}
