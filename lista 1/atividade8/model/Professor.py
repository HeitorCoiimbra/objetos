from model.Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, titulacao):
        super().__init__(nome)
        self.__titulacao = titulacao

    def getTitulacao(self):
        return self.__titulacao

    def setTitulacao(self, titulacao):
        self.__titulacao = titulacao

    def descricao(self):
        return f"{self.getNome()}, {self.getTitulacao()}"