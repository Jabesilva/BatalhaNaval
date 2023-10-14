from abc import ABC, abstractmethod

class Barco(ABC):
    @abstractmethod
    def __init__(self, tamanho: int, tipo: str, posicao):
        self.__tamanho = tamanho
        self.__tipo = tipo
        self.__posicao = posicao
    
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
    
    