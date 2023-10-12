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


    def mostra_jogador(self, nome: str, datnascimento: str, id: int):
        print("NOME DO JOGADOR: ", nome)
        print("NASCIMENTO DO JOGADOR: ", datnascimento)
        print("ID DO JOGADOR: ", id)
        print("\n")

    def procurar_jogador(self):
        print('Por favor, informe o ID do jogador')
        idjogador = input('ID:')

        return idjogador

    def tela_cadastro(self):
        
        nome = input('nome: ')
        data = input('sua data de nascimento: ')

        return {'nome' : nome, 'data' : data}

    def mensagem(self, msg):
        print(msg)