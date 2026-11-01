from model.ContaBancaria import ContaBancaria

def principal():
    c1 = ContaBancaria("Ronaldo", 100)
    c2 = ContaBancaria("Hanna")
    c1.exibirExtrato()
    try:
        c1.sacar(70)
    except ValueError as erro:
        print(erro)
    c1.exibirExtrato()
    try:
        c1.depositar(70)
    except ValueError as erro:
        print(erro)
    c1.exibirExtrato()

    try:
        c1.transferir(c2, 100)
    except ValueError as erro:
        print(erro)
    finally:
        c1.exibirExtrato()
        c2.exibirExtrato()

if __name__ == "__main__":
    principal()