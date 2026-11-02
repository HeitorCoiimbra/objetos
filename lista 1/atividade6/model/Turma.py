class Turma:
    def __init__(self, codigo: str, professor, disciplina):
        self.__codigo = codigo
        self.__professor = professor  # Guarda o objeto Professor
        self.__disciplina = disciplina  # Guarda o objeto Disciplina
        self.__alunos = []  # Lista de objetos Aluno

    def addAluno(self, aluno):
        self.__alunos.append(aluno)  # Adiciona um aluno à turma

    def removeAluno(self, aluno):
        if aluno in self.__alunos:
            self.__alunos.remove(aluno)  # Remove o aluno, se estiver na turma

    def nomeProfessor(self):
        return self.__professor.getNome()  # Retorna o nome do professor

    def nomesAlunos(self):
        nomes = []

        for aluno in self.__alunos:  # Percorre os alunos da turma
            nomes.append(aluno.getNome())  # Guarda cada nome

        return nomes

    def alunoEstaNaTurma(self, aluno):
        return aluno in self.__alunos  # Verifica se o aluno está na lista

    def getDisciplina(self):
        return self.__disciplina  # Retorna o objeto Disciplina

    def getAlunos(self):
        return self.__alunos  # Permite consultar a lista de alunos