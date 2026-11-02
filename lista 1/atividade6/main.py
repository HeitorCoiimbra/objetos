from model.Aluno import Aluno
from model.Professor import Professor
from model.Disciplina import Disciplina
from model.Turma import Turma
from model.Curso import Curso

def principal():
    # Cria a disciplina e o professor
    mat = Disciplina("Orientação a Objetos")
    prof = Professor("Marcos")

    # Cria os alunos
    ana, bia, caio = Aluno("Ana"), Aluno("Bia"), Aluno("Caio")

    # Cria as turmas e adiciona os alunos
    t1 = Turma("T1", prof, mat)
    t1.addAluno(ana)
    t1.addAluno(bia)

    t2 = Turma("T2", prof, mat)
    t2.addAluno(bia)
    t2.addAluno(caio)

    # Cria o curso e adiciona as turmas
    curso = Curso("Sistemas de Informação")
    curso.addTurma(t1)
    curso.addTurma(t2)

    # Testa consultas de professor, alunos e disciplinas
    print(t1.nomeProfessor())
    print(t1.nomesAlunos())
    print(curso.nomesAlunos())
    print(curso.nomesDisciplinas())

    # Testa se os alunos pertencem às turmas e ao curso
    print(curso.alunoEstaNoCurso(caio))
    print(t1.alunoEstaNaTurma(caio))

    # Remove Bia da primeira turma e verifica se ainda está no curso
    t1.removeAluno(bia)
    print(t1.nomesAlunos())
    print(curso.alunoEstaNoCurso(bia))

    # Remove a segunda turma e consulta os alunos restantes
    curso.removeTurma(t2)
    print(curso.nomesAlunos())

if __name__ == "__main__":
    principal()