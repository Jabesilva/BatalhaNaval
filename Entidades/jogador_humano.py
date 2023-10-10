class JogadorHumano(Jogador):
    def __init__(self, nome:str, datnascimento: str, pontuacao: int, jogadas, partidas ):
        super().__init__(pontuacao, jogadas, partidas)
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(datnascimento, str):
            self.__datnascimento = datnascimento
            self.__id = random.ramdint(1,1000)

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def datnascimento(self):
        return self.__nome
    
    @datnascimento.setter
    def datnascimento(self, datnascimento):
        self.__datnascimento = datnascimento

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id