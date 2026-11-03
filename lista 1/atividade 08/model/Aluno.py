from abc import ABC, abstractmethod
from model.Pessoa import Pessoa

class Aluno(Pessoa, ABC):
    def __init__(self, nome, matricula, nota1: float, nota2: float):
        super().__init__(nome)
        self.__matricula = matricula
        self.__nota1 = nota1
        self.__nota2 = nota2

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getNota1(self):
        return self.__nota1

    def setNota1(self, nota1):
        self.__nota1 = nota1

    def getNota2(self):
        return self.__nota2

    def setNota2(self, nota2):
        self.__nota2 = nota2

    def calcularMedia(self):
        return (self.__nota1 + self.__nota2) / 2

    def situacao(self):
        return f"{self.getMatricula()} - {self.getNome()}: {self.aprovado()}"

    @abstractmethod
    def aprovado(self):
        pass