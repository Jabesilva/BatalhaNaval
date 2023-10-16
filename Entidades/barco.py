from abc import ABC, abstractmethod

class Barco(ABC):
    @abstractmethod
    def __init__(self, tamanho: int, tipo: str, posicao_linha: int, posicao_coluna: int):
        self.__tamanho = tamanho
        self.__tipo = tipo
        self.__posicao_linha = posicao_linha
        self.__posicao_coluna = posicao_coluna
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho: int):
        self.__tamanho = tamanho

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo = tipo

    @property
    def posicao_linha(self):
        return self.__posicao_linha
    
    @posicao_linha.setter
    def posicao_linha(self,posicao_linha):
        self.__posicao_linha = posicao_linha
    
    @property
    def posicao_coluna(self):
        return self.__posicao_coluna
    
    @posicao_coluna.setter
    def posicao_coluna(self,posicao_coluna):
        self.__posicao_coluna = posicao_coluna
    