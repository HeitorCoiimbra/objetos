from calendar import monthrange
from datetime import datetime

class Funcionario:
    def __init__(self, nome, cargo):
        # Cargo é obrigatório; ocorrências e dependentes são opcionais.
        self.__nome = nome
        self.__cargo = cargo
        self.__ocorrencias = []
        self.__dependentes = []

    def getNome(self):
        return self.__nome

    def getCargo(self):
        return self.__cargo

    def addOcorrencias(self, ocorrencia):
        self.__ocorrencias.append(ocorrencia)

    def addDependentes(self, dependente):
        self.__dependentes.append(dependente)

    def calcularSalarioLiquido(self, mes, ano):
        # 1. Começa com o salário bruto do cargo.
        salario = self.__cargo.getSalarioBruto()

        # 2. Soma acréscimos e subtrai descontos do mês e ano informados.
        for ocorrencia in self.__ocorrencias:
            data = ocorrencia.getData()

            if data.month == mes and data.year == ano:
                salario += ocorrencia.getAcrescimo()
                salario -= ocorrencia.getDesconto()

        # 3. Descobre o último dia do mês de cálculo.
        ultimoDia = monthrange(ano, mes)[1]
        dataReferencia = datetime(ano, mes, ultimoDia)

        # Acrescenta R$ 100 por dependente com menos de 18 anos.
        for dependente in self.__dependentes:
            idade = dependente.calcularIdade(dataReferencia)

            if idade < 18:
                salario += 100.0

        # 4. Devolve o salário calculado.
        return salario

    def gerarDemonstrativo(self, mes, ano):
        salario = self.calcularSalarioLiquido(mes, ano)

        try:
            with open(f"demonstrativo_{mes}_{ano}.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write(f"Funcionário: {self.__nome}\n")
                arquivo.write(f"Cargo: {self.__cargo.getNome()}\n")
                arquivo.write(f"Competência: {mes:02d}/{ano}\n")
                arquivo.write(f"Salário bruto: R$ {self.__cargo.getSalarioBruto():.2f}\n")
                arquivo.write(f"Salário líquido: R$ {salario:.2f}\n")

        except OSError as erro:
            print(f"Erro ao salvar demonstrativo: {erro}")

        finally:
            print("Finalizada a tentativa de gerar o demonstrativo.")