from abc import ABC, abstractmethod

class Jogador(ABC):
    @abstractmethod
    def __init__(self, pontuacao: int, jogadas, partidas):
        if isinstance(pontuacao, int):
            self.__pontuacao = pontuacao
        self.__jogadas = []
        self.__partidas = []
    
    #Métodos pontuação:

    @property
    def pontuacao(self):
        return self.__pontuacao
    
    @pontuacao.setter
    def pontuacao(self, pontuacao: int):
        if isinstance(pontuacao, int):
            self.__pontuacao = pontuacao

    #Métodos Jogadas:

    def add_jogadas(self, jogada):
        self.__jogadas.append(jogada)

    def rem_jogadas(self, jogada):
        if jogada in self.__jogadas:
            self.__jogadas.remove(jogada)
        else:
            print ("jogada não encontrada!")
    
    def alterar_jogadas(self, numjogada, novajogada):
        self.__jogadas[numjogada] = novajogada
    
    def listar_jogadas(self):
        return self.__jogadas
    
    #Métodos partidas:
    
    def add_partidas(self, partida):
        self.__partidas.append(partida)

    def rem_partidas(self, partida):
        if partida in self.__partidas:
            self.__partidas.remove(partida)
        else:
            print ("Partida não encontrada!")
    
    def alterar_partidas(self, numpartida, novapartida):
        self.__partidas[numpartida] = novapartida
    
    def listar_partidas(self):
        return self.__partidas