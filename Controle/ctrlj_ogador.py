from Entidades.jogador import Jogador

class ControladorJogador:
    def __init__ (self, controladorjogo):
        self.__jogadores = []
        self.__telajogador = Telajogador
        self.__controladorjogo = controladorjogo

    def consultajogador(self, id: int):
        for jogador in self.__jogadores:
            if JogadorHumano