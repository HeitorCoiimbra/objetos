class Dependente:
    def __init__(self, nome, dataNascimento):
        self.__nome = nome
        self.__dataNascimento = dataNascimento

    def getNome(self):
        return self.__nome

    def getDataNascimento(self):
        return self.__dataNascimento

    def calcularIdade(self, dataReferencia):
        nascimento = self.__dataNascimento

        idade = dataReferencia.year - nascimento.year

        if (dataReferencia.month, dataReferencia.day) < (nascimento.month, nascimento.day):
            idade -= 1

        return idade