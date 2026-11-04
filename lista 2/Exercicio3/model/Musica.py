class Musica:
    def __init__(self, titulo: str, artista: str, duracao: int):
        self.__titulo = titulo
        self.__artista = artista
        self.__duracao = duracao

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista

    def getDuracao(self):
        return self.__duracao