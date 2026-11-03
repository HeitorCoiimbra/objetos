from model.Dependente import Dependente
from datetime import datetime

class Funcionario:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__dependentes = []

    def getNome(self):
        return self.__nome

    def addDependentes(self, dependente: Dependente):
        self.__dependentes.append(dependente)
        dependente.setPessoa(self)

    def listarDependentes(self, dataAtual: datetime):
        print(f"Dependentes de {self.__nome}")

        for dependente in self.__dependentes:
            nascimento = dependente.getDataNascimento()
            aniversario = dependente.proximoAniversario(dataAtual)

            print(
                f"{dependente.getNome()} | "
                f"nascimento: {nascimento.strftime('%d/%m/%Y')} | "
                f"próximo aniversário: {aniversario.strftime('%d/%m/%Y')} | "
                f"faltam {dependente.diasParaAniversario(dataAtual)} dias | "
                f"{dependente.diaSemanaAniversario(dataAtual)} | "
            )