from Entidades.jogador_humano import JogadorHumano
from Tela.tela_jogador import Telajogador
import random

class ControladorJogador:
    def __init__(self):
        self.__jogadores = []
        self.__telajogador = Telajogador()
        self.__controladorjogo = []

    def consulta_jogador(self):
        id = int(self.__telajogador.procurar_jogador())
        for jogador in self.__jogadores:
            if jogador.id == id:
                self.__telajogador.mensagem(f'o jogador encontrado é: {jogador.nome}')
    
    def incluir_jogador(self):
        dados_jogador = self.__telajogador.tela_cadastro()
        id = random.randint(1,1000)
        if id in self.__jogadores:
            id = random.randint(1,1000)
        jogador = JogadorHumano(dados_jogador['nome'], dados_jogador['data'], id)
        self.__jogadores.append(jogador)
        self.__telajogador.mensagem('jogador adicionado!')
        self.__telajogador.mensagem(f'seu ID é: { jogador.id }')

    def listar_jogadores(self):
        for jogador in self.__jogadores:
            self.__telajogador.mostra_jogador(jogador.nome, jogador.datnascimento, jogador.id)

    def excluir_jogadores(self):
        self.listar_jogadores()
        idjogador = int(self.__telajogador.procurar_jogador())
        
        for jogador in self.__jogadores:
            if jogador.id == idjogador:
                self.__jogadores.remove(jogador)
                self.__telajogador.mensagem('jogador excluído!')

    def alterar_jogador(self):
        self.listar_jogadores()
        idjogador = self.__telajogador.procurar_jogador()
        for jogador in self.__jogadores:
            if jogador.id == idjogador:
                novos_dados = self.__telajogador.tela_cadastro()
                jogador.nome = novos_dados['nome']
                jogador.datnascimento = novos_dados['data']
                jogador.id = random.randint(1,1000)
                self.__telajogador.mensagem('dados alterados!')
    