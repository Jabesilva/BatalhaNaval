from Entidades.jogador_humano import JogadorHumano
from Tela.tela_jogador import Telajogador
import random

class ControladorJogador:
    def __init__(self, controlador_jogo):
        self.__jogadores = []
        self.__tela_jogador = Telajogador()
        self.__controlador_jogo = controlador_jogo

    def consulta_jogador(self):
        id = int(self.__tela_jogador.procurar_jogador())
        for jogador in self.__jogadores:
            if jogador.id == id:
                self.__tela_jogador.mensagem(f'o jogador encontrado é: {jogador.nome},{jogador.datnascimento},{jogador.id}')
    
    def incluir_jogador(self):
        dados_jogador = self.__tela_jogador.tela_cadastro()
        id = random.randint(1,1000)
        if id in self.__jogadores:
            id = random.randint(1,1000)
        jogador = JogadorHumano(dados_jogador['nome'], dados_jogador['data'], id)
        self.__jogadores.append(jogador)
        self.__tela_jogador.mensagem('jogador adicionado!')
        self.__tela_jogador.mensagem(f'seu ID é: { jogador.id }')

    def listar_jogadores(self):
        for jogador in self.__jogadores:
            self.__tela_jogador.mostra_jogador(jogador.nome, jogador.datnascimento, jogador.id)

    def excluir_jogadores(self):
        self.listar_jogadores()
        idjogador = int(self.__tela_jogador.procurar_jogador())
        
        for jogador in self.__jogadores:
            if jogador.id == idjogador:
                self.__jogadores.remove(jogador)
                self.__tela_jogador.mensagem('jogador excluído!')

    def alterar_jogador(self):
        self.listar_jogadores()
        idjogador = int(self.__tela_jogador.procurar_jogador())
        for jogador in self.__jogadores:
            if jogador.id == idjogador:
                novos_dados = self.__tela_jogador.tela_cadastro()
                jogador.nome = novos_dados['nome']
                jogador.datnascimento = novos_dados['data']
                jogador.id = random.randint(1,1000)
                self.__tela_jogador.mensagem(f'dados alterados!,seu novo ID é: {jogador.id}')
            else:
                self.__tela_jogador.mensagem('jogador não encontrado!')

    def retornar(self):
        self.__controlador_jogo.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_jogador, 2: self.alterar_jogador, 3: self.listar_jogadores, 4: self.excluir_jogadores, 5: self.consulta_jogador, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_jogador.tela_opcoes()]()
