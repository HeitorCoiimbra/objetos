class Curso:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__turmas = []  # Lista de objetos Turma

    def addTurma(self, turma):
        self.__turmas.append(turma)  # Adiciona uma turma ao curso

    def removeTurma(self, turma):
        if turma in self.__turmas:
            self.__turmas.remove(turma)  # Remove a turma do curso

    def nomesAlunos(self):
        nomes = []

        for turma in self.__turmas:  # Percorre as turmas do curso
            for aluno in turma.getAlunos():  # Percorre os alunos de cada turma
                if aluno.getNome() not in nomes:  # Evita nomes repetidos
                    nomes.append(aluno.getNome())

        return nomes

    def nomesDisciplinas(self):
        nomes = []

        for turma in self.__turmas:
            # Obtém o nome da disciplina de cada turma
            nome = turma.getDisciplina().getNome()

            if nome not in nomes:  # Evita disciplinas repetidas
                nomes.append(nome)

        return nomes

    def alunoEstaNoCurso(self, aluno):
        for turma in self.__turmas:  # Verifica todas as turmas
            if turma.alunoEstaNaTurma(aluno):
                return True  # Encontrou o aluno em uma turma

        return False  # Não encontrou em nenhuma turma