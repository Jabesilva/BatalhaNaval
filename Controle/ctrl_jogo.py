from Tela.tela_jogo import TelaJogo
from Controle.ctrl_jogador import ControladorJogador
from Controle.ctrl_oceano import ControladorOceano


class ControladorJogo:
    def __init__(self):
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_oceano = ControladorOceano(self)
        self.__tela_jogo = TelaJogo()

    
    @property
    def controlador_jogador(self):
        return self.__controlador_jogador

    @property
    def controlador_oceano(self):
        return self.__controlador_oceano
    
    def inicia_jogo(self):
        self.abre_tela()

    def cadastra_jogador(self):
        self.__controlador_jogador.abre_tela()

    def criar_oceano(self):
        self.controlador_oceano.abre_tela()

    def encerra_jogo(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_jogador, 2: self.criar_oceano, 0: self.encerra_jogo}

        while True:
            opcao = self.__tela_jogo.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()