from Entidades.barco import Barco

class Bote(Barco):
    def __init__(self, tamanho: int, tipo: str, posicao_linha: int, posicao_coluna: int, cor: str):
        super().__init__(tamanho, tipo, posicao_linha, posicao_coluna)
        self.__cor = cor
    
    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self,cor):
        self.__cor = cor
    