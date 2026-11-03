class Funcionario:
    def __init__(self, nome, salarioBruto, totalAcrescimos, totalDescontos):
        self.__nome = nome
        self.__salarioBruto = salarioBruto
        self.__totalAcrescimos = totalAcrescimos
        self.__totalDescontos = totalDescontos

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getSalarioBruto(self):
            return self.__salarioBruto
    
    def setSalarioBruto(self, salarioBruto):
        if salarioBruto < 0:
            raise ValueError("O salário bruto nãpode ser negativo")
        self.__salarioBruto = salarioBruto

    def getTotalAcrescimos(self):
            return self.__totalAcrescimos
    
    def setTotalAcrescimos(self, totalAcrescimos):
        self.__totalAcrescimos = totalAcrescimos

    def getTotalDescontos(self):
            return self.__totalDescontos

    def setTotalDescontos(self, totalDescontos):
        self.__totalDescontos = totalDescontos

    def calcularSalarioLiquido(self):
        return self.__salarioBruto + self.__totalAcrescimos - self.__totalDescontos