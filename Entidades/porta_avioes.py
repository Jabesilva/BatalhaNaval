from Entidades.barco import Barco

class PortaAvioes(Barco):
    def __init__(self, tamanho: int, tipo: str, posicao_linha: int, posicao_coluna: int, num_avioes: int):
        super().__init__(tamanho, tipo, posicao_linha, posicao_coluna)
        self.__num_avioes = num_avioes
    
    @property
    def num_avioes(self):
        return self.__num_avioes
    
    @num_avioes.setter
    def num_avioes(self,num_avioes):
        self.__num_avioes = num_avioes
    