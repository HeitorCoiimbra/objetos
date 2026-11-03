from model.Pais import Pais

class Estado:
    # Estado sempre precisa de um País.
    def __init__(self, nome: str, pais: Pais):
        self.__nome = nome
        self.__pais = pais

    def getNome(self):
        return self.__nome

    def getPais(self):
        return self.__pais