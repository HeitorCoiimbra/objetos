from model.Funcionario import Funcionario

def principal():
    f1 = Funcionario("Ronaldo", 3000.0, 500.0, 200.0)
    print(f1.calcularSalarioLiquido())
    try:
        f1.setSalarioBruto(3500.0)
    except ValueError as erro:
        print(erro)
    print(f1.calcularSalarioLiquido())

    f2 = Funcionario("Hanna", 2500.0, 400.0, 250.0)
    print(f2.calcularSalarioLiquido())
    try:
        f2.setSalarioBruto(3500.0)
    except ValueError as erro:
        print(erro)
    print(f2.calcularSalarioLiquido())
    try:
        f1.setSalarioBruto(-3500.0)
    except ValueError as erro:
        print(erro)

    f1.nome = 'outro'
    print(f1.getNome())
    # O nome não muda porque f1.nome é um atributo diferente de __nome, pra isso que existe o setNome()

if __name__ == "__main__":
    principal()