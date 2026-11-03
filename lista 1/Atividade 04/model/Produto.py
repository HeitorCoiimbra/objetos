class Produto:
    def __init__(self, nome: str, qtdeEstoque: int, estoqueMinimo: int, estoqueMaximo: int):
        self.__nome = nome
        self.__qtdeEstoque = qtdeEstoque
        self.__estoqueMaximo = estoqueMaximo
        self.__estoqueMinimo = estoqueMinimo
        self.__historico = []

    def getNome(self):
        return self.__nome

    def setNome(self, nome: str):
        self.__nome = nome

    def getQtdeEstoque(self):
        return self.__qtdeEstoque

    def getEstoqueMaximo(self):
        return self.__estoqueMaximo

    def setEstoqueMaximo(self, estoqueMaximo: int):
        self.__estoqueMaximo = estoqueMaximo

    def getEstoqueMinimo(self):
        return self.__estoqueMinimo

    def setEstoqueMinimo(self, estoqueMinimo: int):
        self.__estoqueMinimo = estoqueMinimo

    def exibirHistorico(self):
        print(f"Histórico de {self.getNome()}")

        for acao in self.__historico:
            print(acao)

        print(f"Quantidade de {self.getNome()} em estoque: {self.__qtdeEstoque}")

    def debitarEstoque(self, qtde: int):
        if qtde <= 0:
            print("Quantidade inválida")
            return
        self.__qtdeEstoque -= qtde

    def creditarEstoque(self, qtde: int):
        if qtde <= 0:
            print("Quantidade inválida")
            return
        self.__qtdeEstoque += qtde

    def verificarEstoqueBaixo(self):
        if self.__qtdeEstoque < self.__estoqueMinimo:
            return True
        return False

    def verificarEstoqueInsuficiente(self, qtde: int):
        if qtde > self.__qtdeEstoque:
            return True
        return False

    def verificarEstoqueExcedente(self, qtde: int):
        if (self.__qtdeEstoque + qtde) > self.__estoqueMaximo:
            return True
        return False

    def vender(self, qtde: int):
        if self.verificarEstoqueInsuficiente(qtde):
            print("Estoque insuficiente")
            return False
        self.debitarEstoque(qtde)
        self.__historico.append(f"Foram vendidos {qtde} de {self.getNome()}")
        if self.vericarEstoqueBaixo():
            print("Estoque baixo")
        return True

    def comprar(self, qtde: int):
        if self.verificarEstoqueExcedente(qtde):
            print("Estoque excedente")
            return False
        self.creditarEstoque(qtde)
        self.__historico.append(f"Foram comprados {qtde} de {self.getNome()}")
        return True