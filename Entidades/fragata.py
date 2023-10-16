from Entidades.barco import Barco

class Fragata(Barco):
    def __init__(self, tamanho: int, tipo: str, posicao_linha: int, posicao_coluna: int, canhoes: int):
        super().__init__(tamanho, tipo, posicao_linha, posicao_coluna)
        self.__canhoes = canhoes
    
    @property
    def canhoes(self):
        return self.__canhoes
    
    @canhoes.setter
    def canhoes(self,canhoes):
        self.__canhoes = canhoes
    