from model.Assinatura import Assinatura

class PlanoPremium(Assinatura):
    def __init__(self, assinante: str, mesesContrato: int):
        super().__init__(assinante)
        self.__mesesContrato = mesesContrato

    def calcularMensalidade(self) -> float:
        valor = 45.0

        if self.__mesesContrato >= 12:
            valor -= valor * 0.10

        return valor

    def nomePlano(self) -> str:
        return "Plano Premium"