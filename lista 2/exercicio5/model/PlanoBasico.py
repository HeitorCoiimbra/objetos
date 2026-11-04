from model.Assinatura import Assinatura

class PlanoBasico(Assinatura):
    def __init__(self, assinante: str):
        super().__init__(assinante)

    def calcularMensalidade(self) -> float:
        return 20.0

    def nomePlano(self) -> str:
        return "Plano Básico"