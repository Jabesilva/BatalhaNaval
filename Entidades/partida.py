from Entidades.jogador import Jogador
from Entidades.oceano import Oceano

class Partida (self, Oceano, Jogador):
    def __init__(self):
        self.__oceanojogador = Oceano
        self.__oceanocomputador = Oceano
        self.__jogador1 = Jogador
        self.__computador = Jogador
        self.__pontuacaojogador1 = Jogador
        self.__pontuacaocomputador = Jogador

    @property
    def jogador(self):
        return self.__jogador1
    
    @jogador.setter
    def jogador(self, jogador1):
        self.__jogador1 = jogador1
    
    @property
    def computador(self):
        return self.__computador
    
    @jogador.setter
    def computador(self, computador):
        self.__computador = computador
    
    @property
    def oceanojogador1(self):
        return self.__oceanojogador1
    
    @jogador.setter
    def oceanojogador1(self, oceanojogador1):
        self.__computador = computador
