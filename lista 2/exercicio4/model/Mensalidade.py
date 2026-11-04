from datetime import datetime

class Mensalidade:
    def __init__(self, valor: float, vencimento: datetime):
        self.__valor = valor
        self.__vencimento = vencimento
        self.__pago = False

    def getValor(self):
        return self.__valor

    def getVencimento(self):
        return self.__vencimento

    def getPago(self):
        return self.__pago

    def diasAtraso(self, data: datetime) -> int:
        if data <= self.__vencimento:
            return 0

        return (data - self.__vencimento).days

    def calcularTotal(self, data: datetime) -> float:
        dias = self.diasAtraso(data)

        if dias == 0:
            return self.__valor

        multa = self.__valor * 0.02
        juros = dias * 1.50

        total = self.__valor + multa + juros

        return round(total, 2)

    def situacao(self, data: datetime) -> str:
        dias = self.diasAtraso(data)

        if dias == 0:
            return "em dia"

        return f"atrasada há {dias} dias"

    def pagar(self, data: datetime) -> float:
        if self.__pago:
            raise ValueError("Mensalidade já paga")

        total = self.calcularTotal(data)
        self.__pago = True

        return total