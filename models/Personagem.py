class Personagem:

    def __init__(self, nome, raca, classe):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.nivel = 1
        self.atributos = {
        "Forca": 0,
        "Destreza": 0,
        "Constituicao": 0,
        "Inteligencia": 0,
        "Sabedoria": 0,
        "Carisma": 0
    }
