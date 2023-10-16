from Entidades.barco import Barco

class Submarino(Barco):
    def __init__(self, tamanho: int, tipo: str, posicao_linha: int, posicao_coluna: int, profundidade: int):
        super().__init__(tamanho, tipo, posicao_linha, posicao_coluna)
        self.__profundidade = profundidade
    
    @property
    def profundidade(self):
        return self.__profundidade
    
    @profundidade.setter
    def profundidade(self,profundidade):
        self.__profundidade = profundidade
    