

class Oceano():
    def __init__(self, tamanho_linhas: int, tamanho_colunas: int):
        self.__tamanho_linhas = tamanho_linhas
        self.__tamanho_colunas = tamanho_colunas
        self.__matriz = None
    
    def criar_matriz(self):
        self.__matriz = [[0 for _ in range(self.__tamanho_colunas)]for _ in range(self.__tamanho_linhas)]
    
    def imprimir_matriz(self):
        if self.__matriz is not None:
            for linha in self.__matriz:
                print(linha)
    