from datetime import datetime
from math import ceil

class Ticket:
    def __init__(self, placa: str, entrada: datetime):
        self.__placa = placa
        self.__entrada = entrada

    def getPlaca(self):
        return self.__placa

    def getEntrada(self):
        return self.__entrada

    def permanencia(self, saida: datetime) -> int:
        if saida < self.__entrada:
            raise ValueError("Saída anterior à entrada")

        minutos = (saida - self.__entrada).total_seconds() / 60

        return int(minutos)

    def calcularValor(self, saida: datetime) -> float:
        minutos = self.permanencia(saida)

        if minutos <= 15:
            return 0.0

        if minutos <= 60:
            return 8.0

        horasAdicionais = ceil((minutos - 60) / 60)

        valor = 8.0 + (horasAdicionais * 4.0)

        if valor > 40.0:
            return 40.0

        return valor