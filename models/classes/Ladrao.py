from models.classes.Classe import Classe

class Ladrao(Classe):
    def __init__(self):
        super().__init__("Ladrao", 6, 1)
        self.armas = ["Pequenas", "Medias"]
        self.armaduras = ["Leves"]
        self.itens_magicos = ["Pergaminho de protecao"]
        # habilidade : nível necessário para usar habilidade
        self.habilidades = {"Ataque furtivo": 1, "Ouvir ruidos": 1, "Talentos de ladrao": 1}
