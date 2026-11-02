class Disciplina:
    def __init__(self, nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome