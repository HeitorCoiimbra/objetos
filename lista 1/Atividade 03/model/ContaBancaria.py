
class ContaBancaria:
    def __init__(self, titular, saldo = 0.0):
        self.__titular = str(titular)
        self.__saldo = float(saldo)
        self.__historico = []

    def getTitular(self):
        return self.__titular

    def getSaldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido")
            return False

        self.__saldo += valor
        self.__historico.append(f"Depósito de R$ {valor}")
        return True

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")

        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente")

        self.__saldo -= valor
        self.__historico.append(f"Saque de R$ {valor}")
        return True

    def transferir(self, destino, valor):
        if valor <= 0:
            print("Valor inválido")
            return False

        if self.sacar(valor):
            if destino.depositar(valor):
                return True

        return False

    def exibirExtrato(self):
        print(f"Extrato de {self.__titular}")

        for operacao in self.__historico:
            print(operacao)

        print(f"Saldo atual: R$ {self.__saldo}")
