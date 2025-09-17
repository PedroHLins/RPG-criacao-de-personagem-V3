import random

class Dado:
    @staticmethod
    def rolar3d6():
        resultado = []
        for i in range(3):
            resultado.append(random.randrange(1, 7))
        return resultado

    @staticmethod
    def rolar4d6():
        resultado = []
        for i in range(4):
            resultado.append(random.randrange(1, 7))
        return resultado