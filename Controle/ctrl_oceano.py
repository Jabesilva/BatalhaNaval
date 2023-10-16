from Entidades.bote import Bote
from Entidades.fragata import Fragata
from Entidades.submarino import Submarino
from Entidades.porta_avioes import PortaAvioes
from Entidades.oceano import Oceano
from Tela.tela_oceano import TelaOceano
import random

class ControladorOceano:
    def __init__(self, controlador_jogo):
        self.__oceanos = []
        self.__barcos = []
        self.__tela_oceano = TelaOceano()
        self.__controlador_jogo = controlador_jogo

    def gera_oceano(self):
        dados_oceano = self.__tela_oceano.tamanho_ceano()
        codigo = random.randint(1,100)
        if codigo in self.__oceanos:
            codigo = random.randint(1,1000)
        oceano = Oceano(int(dados_oceano['tamanho_linhas']), int(dados_oceano['tamanho_colunas']), codigo)
        oceano.criar_matriz()
        self.__oceanos.append(oceano)
        self.__tela_oceano.mensagem(f'Oceano criado!, o código do oceano é:{oceano.codigo}')
        self.__tela_oceano.mensagem('\n')

    def inclui_barcos(self):
        self.__tela_oceano.mensagem('Você tem 8 barcos para adicionar no seu oceano, 3 botes, 2 submarinos, 2 fragatas e 1 porta-aviões')
        oceanocodigo = int(self.__tela_oceano.selecionar_oceano())
        for oceano in self.__oceanos:
            if oceano.codigo == oceanocodigo:
                for _ in range(3):
                    oceano.mostra_matriz()
                    self.__tela_oceano.mensagem('\n')
                    dados_bote = self.__tela_oceano.incluir_bote()
                    bote = Bote(1, 'bote', int(dados_bote['linha']), int(dados_bote['coluna']), dados_bote['cor'])
                    check = oceano.checa_posicoes(bote,1)
                    if check == False:
                        self.__tela_oceano.mensagem('posição já usada!')
                        break
                    oceano.adicionar_barco(bote)
                    oceano.add_barco_oceano(bote, 2)
                for _ in range(2):
                    oceano.mostra_matriz()
                    self.__tela_oceano.mensagem('\n')
                    dados_submarino = self.__tela_oceano.incluir_submarino()
                    submarino = Submarino(2, 'submarino', int(dados_submarino['linha']), int(dados_submarino['coluna']), dados_submarino['profundidade'])
                    check = oceano.checa_posicoes(submarino,int(dados_submarino['sentido']))
                    if check == False:
                        self.__tela_oceano.mensagem('posição já usada!')
                        break
                    oceano.adicionar_barco(submarino)
                    oceano.add_barco_oceano(submarino, int(dados_submarino['sentido']))
                for _ in range(2):
                    oceano.mostra_matriz()
                    self.__tela_oceano.mensagem('\n')
                    dados_fragata = self.__tela_oceano.incluir_fragata()
                    fragata = Fragata(3, 'fragata', int(dados_fragata['linha']), int(dados_fragata['coluna']), int(dados_fragata['num_canhoes']))
                    check = oceano.checa_posicoes(fragata,int(dados_fragata['sentido']))
                    if check == False:
                        self.__tela_oceano.mensagem('posição já usada!')
                        break                    
                    oceano.adicionar_barco(fragata)
                    oceano.add_barco_oceano(fragata, int(dados_fragata['sentido']))
                
                oceano.mostra_matriz()
                self.__tela_oceano.mensagem('\n')
                dados_portaavioes = self.__tela_oceano.incluir_porta_avioes()
                Porta_avioes = PortaAvioes(4, 'porta-avioes', int(dados_portaavioes['linha']), int(dados_portaavioes['coluna']), int(dados_portaavioes['avioes']))
                check = oceano.checa_posicoes(Porta_avioes,int(dados_portaavioes['sentido']))
                if check == False:
                    self.__tela_oceano.mensagem('posição já usada!')
                    break                
                oceano.adicionar_barco(Porta_avioes)
                oceano.add_barco_oceano(Porta_avioes, int(dados_portaavioes['sentido']))
                oceano.mostra_matriz()
                
    def retornar(self):
        self.__controlador_jogo.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = { 1: self.gera_oceano, 2: self.inclui_barcos, 0: self.retornar }
        
        continua = True
        while continua:
            lista_opcoes[ self.__tela_oceano.tela_opcoes()]()