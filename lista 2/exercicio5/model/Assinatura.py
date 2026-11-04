from abc import ABC, abstractmethod

class Assinatura(ABC):
    def __init__(self, assinante: str):
        self.__assinante = assinante

    def getAssinante(self):
        return self.__assinante

    @abstractmethod
    def calcularMensalidade(self) -> float:
        pass

    @abstractmethod
    def nomePlano(self) -> str:
        pass

    def descricao(self) -> str:
        return f"{self.__assinante}: {self.nomePlano()}, R$ {self.calcularMensalidade():.2f}"