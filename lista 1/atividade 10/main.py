from datetime import datetime
from model.Cargo import Cargo
from model.Ocorrencia import Ocorrencia
from model.Dependente import Dependente
from model.Funcionario import Funcionario


def principal():
    carla = Funcionario("Carla", Cargo("Analista", 5000.0))

    carla.addOcorrencias(
        Ocorrencia(datetime(2026, 9, 10), "Hora extra", acrescimo=300.0)
    )
    carla.addOcorrencias(
        Ocorrencia(datetime(2026, 9, 25), "Falta", desconto=150.0)
    )
    carla.addOcorrencias(
        Ocorrencia(datetime(2026, 10, 5), "Hora extra", acrescimo=400.0)
    )

    carla.addDependentes(Dependente("Lucas", datetime(2015, 3, 10)))
    carla.addDependentes(Dependente("Júlia", datetime(2018, 10, 21)))
    carla.addDependentes(Dependente("Pedro", datetime(2008, 9, 30)))

    print(f"Salário líquido 09/2026: {carla.calcularSalarioLiquido(9, 2026)}")
    print(f"Salário líquido 10/2026: {carla.calcularSalarioLiquido(10, 2026)}")

    funcionario2 = Funcionario("Rafael", Cargo("Assistente", 2500.0))
    print(funcionario2.calcularSalarioLiquido(9, 2026))
    # Desafio extra: grava o demonstrativo de setembro.
    carla.gerarDemonstrativo(9, 2026)


if __name__ == "__main__":
    principal()