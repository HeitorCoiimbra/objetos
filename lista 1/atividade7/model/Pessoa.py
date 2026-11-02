from model.Cidade import Cidade
from model.Escolaridade import Escolaridade

class Pessoa:
    # Pessoa pode não ter cidade natal nem escolaridade informada.
    def __init__(self, nome: str, cidadeNatal: Cidade = None):
        self.__nome = nome
        self.__cidadeNatal = cidadeNatal
        self.__escolaridade = None

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome
    
    def setEscolaridade(self, escolaridade: Escolaridade):
        self.__escolaridade = escolaridade

    def cidadeNascimento(self):
        if self.__cidadeNatal is None:
            return "Não informado"

        return self.__cidadeNatal.getNome()

    def estadoNascimento(self):
        if self.__cidadeNatal is None:
            return "Não informado"

        return self.__cidadeNatal.getEstado().getNome()

    def paisNascimento(self):
        if self.__cidadeNatal is None:
            return "Não informado"

        return self.__cidadeNatal.getEstado().getPais().getNome()

    def escolaridadeDescricao(self):
        if self.__escolaridade is None:
            return "Não informado"

        return self.__escolaridade.getDescricao()