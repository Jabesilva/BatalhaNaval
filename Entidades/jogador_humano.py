from Entidades.jogador import Jogador

class JogadorHumano(Jogador):
    def __init__(self, nome:str, datnascimento: str, id):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(datnascimento, str):
            self.__datnascimento = datnascimento
        self.__id = id

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def datnascimento(self):
        return self.__datnascimento
    
    @datnascimento.setter
    def datnascimento(self, datnascimento: str):
        self.__datnascimento = datnascimento

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id: int):
        self.__id = id