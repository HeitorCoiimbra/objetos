from model.Aluno import Aluno
class AlunoGraduacao(Aluno.Aluno):
    def __init__(self, nome, matricula, nota1, nota2):
        super().__init__(nome, matricula, nota1, nota2)

    def aprovado(self):
        if self.calcularMedia() >= 7:
            return "aprovado"
        return "reprovado"