from abc import ABC, abstractmethod

class Jogador(ABC):
    @abstractmethod
    def __init__(self):
        self.__pontuacao = None
        self.__jogadas = []
        self.__partidas = []
    
    #Métodos pontuação:

    @property
    def pontuacao(self):
        return self.__pontuacao
    
    @pontuacao.setter
    def pontuacao(self, pontuacao):
        self.__pontuacao = pontuacao

    #Métodos Jogadas:

    def add_jogadas(self, jogada):
        self.__jogadas.append(jogada)
    
    def listar_jogadas(self):
        return self.__jogadas
    
    #Métodos partidas:
    
    def add_partidas(self, partida):
        self.__partidas.append(partida)
    
    def listar_partidas(self):
        return self.__partidas