from model.Pessoa import Pessoa

class Aluno(Pessoa):  # Aluno herda de Pessoa
    def __init__(self, nome: str):
        super().__init__(nome) # Usa o construtor da classe Pessoa