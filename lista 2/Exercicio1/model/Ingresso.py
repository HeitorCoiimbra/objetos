
class Ingresso:
    def __init__(self, filme: str, valorBase: float):
        self.__filme = filme
        self.setValorBase(valorBase)

    def getFilme(self):
        return self.__filme

    def setFilme(self, filme: str):
        self.__filme = filme

    def getValorBase(self):
        return self.__valorBase

    def setValorBase(self, valorBase: float):
        if valorBase <= 0:
            raise ValueError("Valor base deve ser maior que zero")
        self.__valorBase = valorBase

    def calcularValor(self, tipo: str):
        tipos = {
            "inteira": 1.0,
            "meia": 0.5,
            "idoso": 0.4
        }

        tipo = tipo.lower()

        if tipo not in tipos:
            raise ValueError(f"Tipo de ingresso inválido: {tipo}")

        return self.getValorBase() * tipos[tipo]