from abc import ABC, abstractmethod

class Jogador(ABC):
    @abstractmethod
    def __init__(self):
        self.__pontuacao = 0
        self.__jogadas = []
        self.__partidas = []
    
    #Métodos pontuação:

    @property
    def pontuacao(self):
        return self.__pontuacao
    
    @pontuacao.setter
    def add_pontuacao(self, pontuacao: int):
        self.__pontuacao += pontuacao

    #Métodos Jogadas:

    def add_jogadas(self, jogada):
        self.__jogadas.append(jogada)
    
    def listar_jogadas(self):
        for jogada in self.__jogadas:
            return jogada
    
    #Métodos partidas:
    
    def add_partidas(self, partida):
        self.__partidas.append(partida)
    
    def listar_partidas(self):
        for partida in self.__partidas:
            return partida