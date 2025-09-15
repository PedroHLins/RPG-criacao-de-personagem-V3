from models.racas.Raca import Raca

class Humano(Raca):
    def __init__(self):
        super().__init__("Humano", 9, 0, "Qualquer")
        self.habilidades = ["Aprendizado", "Adaptabilidade"]
