class Playlist:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__musicas = []

    def getNome(self):
        return self.__nome

    def addMusica(self, musica):
        for m in self.__musicas:
            if m.getTitulo() == musica.getTitulo() and m.getArtista() == musica.getArtista():
                return False

        self.__musicas.append(musica)
        return True

    def removeMusica(self, titulo: str):
        for m in self.__musicas:
            if m.getTitulo() == titulo:
                self.__musicas.remove(m)
                return True

        return False

    def duracaoTotal(self) -> str:
        total = 0

        for m in self.__musicas:
            total += m.getDuracao()

        minutos = total // 60
        segundos = total % 60

        return f"{minutos:02d}:{segundos:02d}"

    def musicaMaisLonga(self):
        if len(self.__musicas) == 0:
            return None

        maior = self.__musicas[0]

        for m in self.__musicas:
            if m.getDuracao() > maior.getDuracao():
                maior = m

        return maior

    def musicasDoArtista(self, artista: str) -> list:
        musicas = []

        for m in self.__musicas:
            if m.getArtista() == artista:
                musicas.append(m.getTitulo())

        return musicas