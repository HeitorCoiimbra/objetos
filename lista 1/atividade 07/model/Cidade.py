from model.Estado import Estado

class Cidade:
    # Cidade sempre precisa de um Estado.
    def __init__(self, nome: str, estado: Estado):
        self.__nome = nome
        self.__estado = estado

    def getNome(self):
        return self.__nome

    def getEstado(self):
        return self.__estado