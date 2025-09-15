from models.racas.Raca import Raca

class Anao(Raca):
    def __init__(self):
        super().__init__("Anao", 6, 18, "Ordem")
        self.habilidades = ["Vigoroso", "Armas grandes", "Inimigos"]
