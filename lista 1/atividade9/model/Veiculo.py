from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, placa, valor):
        super().__init__()
        self.__placa = placa
        self.__valor = valor
        self.__alugado = False
        self.__historico = []

    def getPlaca(self):
        return self.__placa

    def setPlaca(self, placa):
        self.__placa = placa

    def getValor(self):
        return self.__valor

    def setValor(self, valor):
        self.__valor = valor

    @abstractmethod
    def calcularAluguel(self, dias):
        pass

    def alugar(self, cliente, dias):
        if self.__alugado:
            print(f"Veículo de placa {self.getPlaca()} não disponível para aluguel")
            return False

        if dias <= 0:
            print("Número de dias inválido")
            return False

        valorAluguel = self.calcularAluguel(dias)
        self.__alugado = True

        self.__historico.append(f"Veículo placa {self.getPlaca()} alugado pelo cliente {cliente.getNome()} no valor de R$ {valorAluguel}")

        print(f"Aluguel confirmado para o veículo de placa {self.getPlaca()}")
        return True

    def devolver(self):
        if not self.__alugado:
            print(f"Veículo de placa {self.getPlaca()} não estava alugado")
            return False

        self.__alugado = False
        self.__historico.append(f"Veículo placa {self.getPlaca()} devolvido")

        print(f"Devolução realizada para o veículo de placa {self.getPlaca()}")
        return True

    def listarHistorico(self):
        print(f"Histórico do veículo de placa {self.getPlaca()}")

        for acao in self.__historico:
            print(acao)