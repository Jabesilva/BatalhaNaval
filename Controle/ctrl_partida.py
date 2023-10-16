from Entidades.partida import Partida
from Tela.tela_partida import TelaPartida

class ControladorJogo:
    def __init__(self, controlador_jogo):
        self.__controlador_jogo = controlador_jogo
        self.__partidas = []
        self.__tela_partida = TelaPartida()