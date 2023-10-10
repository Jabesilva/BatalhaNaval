import random

class Telajogador():
    def tela_login(self):
        print('      -- Jogador --     ')
        print('     1   -   Login      ')
        print('     2   -  Cadastrar   ')
        
        opcao = int(input('escolha a opcao: '))

        return opcao
    
    def tela_opcoes(self):
        print(' -- Opcoes jogador --  ')
        print(' 1 - consultar jogador ')
        print(' 2 - exluir jogador    ')
        print(' 3 - alterar jogador   ')
        print(' 4 - adicionar jogador ')

    def tela_cadastro(self):
        print(' bem-vindo! ')
        
        nome = input('nome: ')
        data = input('sua data de nascimento: ')

    def mensagem(self, msg)
        print(msg)