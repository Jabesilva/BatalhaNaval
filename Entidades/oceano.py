from Entidades.bote import Bote
from Entidades.fragata import Fragata
from Entidades.submarino import Submarino
from Entidades.porta_avioes import PortaAvioes


class Oceano():
    def __init__(self, tamanho_linhas: int, tamanho_colunas: int, codigo: int):
        self.__tamanho_linhas = tamanho_linhas
        self.__tamanho_colunas = tamanho_colunas
        self.__matriz = None
        self.__codigo = codigo
        self.__barcos = []
    
    def criar_matriz(self):
        self.__matriz = [[0 for _ in range(self.__tamanho_colunas)]for _ in range(self.__tamanho_linhas)]
    
    def mostra_matriz(self):
        if self.__matriz is not None:
            for linha in self.__matriz:
                print(linha)
    
    def adicionar_barco(self, barco):
        self.__barcos.append(barco)

    def listar_barcos(self):
        for barco in self.__barcos:
            return f"Barco: {barco.tipo}, Comprimento: {barco.tamanho}"

    
    def add_barco_oceano(self, barco, sentido):
            if barco.posicao_linha > self.__tamanho_linhas or barco.posicao_coluna > self.__tamanho_colunas:
                return "Posição inválida para o barco."
            else:
                for i in range(barco.tamanho):
                    if sentido == 2 :
                        if ((barco.posicao_coluna + barco.tamanho) - 1) > self.__tamanho_colunas:
                            return "Barco fora do tamanho do oceano"
                            break
                        else:
                            self.__matriz[barco.posicao_linha - 1][(barco.posicao_coluna - 1) + i] = 1
                    else:
                        if ((barco.posicao_linha + barco.tamanho) - 1) > self.__tamanho_linhas:
                            return "Barco fora do tamanho do oceano"
                            break              
                        else:
                            self.__matriz[(barco.posicao_linha - 1) + i][barco.posicao_coluna - 1] = 1
    
    def checa_posicoes(self,barco,sentido):
        for i in range(barco.tamanho):
            if sentido == 2 :
                if self.__matriz[barco.posicao_linha - 1][(barco.posicao_coluna - 1) + i] == 0:
                    pass
                else:
                    return False        
            else:
                if self.__matriz[(barco.posicao_linha - 1) + i][barco.posicao_coluna - 1] == 0:
                    pass
                else:
                    return False
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

