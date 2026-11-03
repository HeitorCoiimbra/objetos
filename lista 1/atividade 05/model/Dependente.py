from datetime import datetime

class Dependente:
    def __init__(self, nome: str, dataNascimento: datetime):
        self.__nome = nome
        self.__dataNascimento = dataNascimento
        self.__pessoa = None

    def getNome(self):
        return self.__nome

    def getDataNascimento(self):
        return self.__dataNascimento

    def setPessoa(self, pessoa):
        self.__pessoa = pessoa

    def getPessoa(self):
        return self.__pessoa

    def proximoAniversario(self, dataAtual: datetime):
        ano = dataAtual.year

        try:
            aniversario = datetime(ano, self.__dataNascimento.month, self.__dataNascimento.day)
        except ValueError:
            aniversario = datetime(ano, 2, 28)

        if aniversario.date() < dataAtual.date():
            ano += 1

            try:
                aniversario = datetime(ano, self.__dataNascimento.month, self.__dataNascimento.day)
            except ValueError:
                aniversario = datetime(ano, 2, 28)

        return aniversario

    def diasParaAniversario(self, dataAtual: datetime):
        aniversario = self.proximoAniversario(dataAtual)
        diferenca = aniversario.date() - dataAtual.date()
        return diferenca.days

    def diaSemanaAniversario(self, dataAtual: datetime):
        aniversario = self.proximoAniversario(dataAtual)

        diasSemana = [
            "Segunda-feira",
            "Terça-feira",
            "Quarta-feira",
            "Quinta-feira",
            "Sexta-feira",
            "Sábado",
            "Domingo"
        ]

        return diasSemana[aniversario.weekday()]