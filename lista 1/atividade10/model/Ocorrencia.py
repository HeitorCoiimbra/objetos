class Ocorrencia:
    def __init__(self, data, descricao, acrescimo=0.0, desconto=0.0):
        self.__data = data
        self.__descricao = descricao
        self.__acrescimo = acrescimo
        self.__desconto = desconto

    def getData(self):
        return self.__data

    def getDescricao(self):
        return self.__descricao

    def getAcrescimo(self):
        return self.__acrescimo

    def getDesconto(self):
        return self.__desconto