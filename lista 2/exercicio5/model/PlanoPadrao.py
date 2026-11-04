from model.Assinatura import Assinatura

class PlanoPadrao(Assinatura):
    def __init__(self, assinante: str, telas: int):
        super().__init__(assinante)

        if telas < 1 or telas > 4:
            raise ValueError("Número de telas deve ser de 1 a 4")

        self.__telas = telas

    def calcularMensalidade(self) -> float:
        valor = 30.0

        if self.__telas > 2:
            valor += (self.__telas - 2) * 5.0

        return valor

    def nomePlano(self) -> str:
        return "Plano Padrão"