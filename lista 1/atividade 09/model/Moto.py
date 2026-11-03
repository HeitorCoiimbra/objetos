from model.Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, placa, valor):
        super().__init__(placa, valor)

    def calcularAluguel(self, dias):
        if dias < 30:
            return round((self.getValor() * dias) * 1.2, 2)
        return round((self.getValor() * dias) * 1.1, 2)