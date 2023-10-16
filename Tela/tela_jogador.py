class Telajogador():
    
    def tela_opcoes(self):
        print(' -- Opcoes jogador -- ')
        print(' 1 - incluir jogador  ')
        print(' 2 - alterar jogador  ')
        print(' 3 - listar jogadores ')
        print(' 4 - excluir jogador  ')
        print(' 5 - consultar jogador')
        print(' 0 -     retornar     ')

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostra_jogador(self, nome: str, datnascimento: str, id: int):
        print("NOME DO JOGADOR: ", nome)
        print("DATA DENASCIMENTO DO JOGADOR: ", datnascimento)
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