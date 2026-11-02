from model.Pais import Pais
from model.Estado import Estado
from model.Cidade import Cidade
from model.Escolaridade import Escolaridade
from model.Pessoa import Pessoa


def principal():
    br = Pais("Brasil")
    mg = Estado("Minas Gerais", br)
    jf = Cidade("Juiz de Fora", mg)

    ana = Pessoa("Ana", jf)
    ana.setEscolaridade(Escolaridade("Superior completo"))

    bruno = Pessoa("Bruno")

    print(ana.paisNascimento())
    print(ana.estadoNascimento())
    print(ana.escolaridadeDescricao())
    print(bruno.paisNascimento())


if __name__ == "__main__":
    principal()