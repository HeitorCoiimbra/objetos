class Pessoa:
    def __init__(self, sexo, peso, altura):
        self.__sexo = str(sexo)
        self.__peso = float(peso)
        self.__altura = float(altura)

    def getSexo(self):
        return self.__sexo

    def setSexo(self, sexo):
        self.__sexo = str(sexo)

    def getPeso(self):
        return self.__peso

    def setPeso(self, peso):
        self.__peso = float(peso)

    def getAltura(self):
        return self.__altura

    def setAltura(self, altura):
        self.__altura = float(altura)

    def calcularImc(self):
        imc = self.__peso / (self.__altura ** 2)

        if self.__sexo == "F":
            if imc < 19.1:
                return "abaixo do peso"
            if imc < 25.8:
                return "no peso normal"
            if imc < 27.3:
                return "marginalmente acima do peso"
            if imc < 32.3:
                return "acima do peso ideal"
            return "obeso"

        if self.__sexo == "M":
            if imc < 20.7:
                return "abaixo do peso"
            if imc < 26.4:
                return "no peso normal"
            if imc < 27.8:
                return "marginalmente acima do peso"
            if imc < 31.1:
                return "acima do peso ideal"
            return "obeso"