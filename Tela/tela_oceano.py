class TelaOceano:
    def tela_opcoes(self):
        print("-------- Opcoes Oceano ----------")
        print("Escolha a opcao")
        print("1 - Gerar oceano")
        print("2 - Adicionar barcos ao oceano")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao: "))
        return opcao


    def tamanho_ceano(self):
        print(' por favor, informe o tamanho do seu oceano. ')
        print('\n')
        tamanho_lin = input('numero de linhas:')
        tamanho_colun = input('numero de colunas:')

        return { 'tamanho_linhas': tamanho_lin, 'tamanho_colunas': tamanho_colun }
    
    def incluir_bote(self):
        print('---- Selecione o lugar do Bote ---- ')
        print('\n')        
        linha = input('linha:')
        coluna = input('coluna:')
        cor = input('cor do bote:')

        return { 'linha': linha, 'coluna': coluna, 'cor': cor }
    
    def incluir_submarino(self):
        print('---- Selecione o lugar do Submarino, e o seu sentido ---- ')
        print('\n')
        print(' depois, selecione 1 ou 2: ')
        print(' 1 - Vertical')
        print(' 2 - horizontal')
        print('\n')
        linha = input('linha:')
        coluna = input('coluna:')
        sentido = input('Sentido:')
        profundidade = input('profundidade do submarino:')

        return { 'linha': linha, 'coluna': coluna, 'sentido': sentido, 'profundidade': profundidade }

    def incluir_fragata(self):
        print('---- Selecione o lugar da Fragata, e o seu sentido ---- ')
        print('\n')
        print(' depois, selecione 1 ou 2: ')
        print(' 1 - Vertical')
        print(' 2 - horizontal')
        print('\n')
        linha = input('linha:')
        coluna = input('coluna:')
        sentido = input('Sentido:')
        num_canhoes = input('numero de canhoes da Fragata:')

        return { 'linha': linha, 'coluna': coluna, 'sentido': sentido, 'num_canhoes': num_canhoes }  

    def incluir_porta_avioes(self):
        print('---- Selecione o lugar do porta avioes, e o seu sentido ---- ')
        print('\n')
        print(' depois, selecione 1 ou 2: ')
        print(' 1 - Vertical')
        print(' 2 - horizontal')
        print('\n')
        linha = input('linha:')
        coluna = input('coluna:')
        sentido = input('Sentido:')
        avioes = input('numero de avioes do porta_avioes:')

        return { 'linha': linha, 'coluna': coluna, 'sentido': sentido, 'avioes': avioes }  

    def selecionar_oceano(self):
        print('por favor, selecione seu oceano pelo código:')
        print('\n')
        codigo = input('codigo do oceano:')

        return codigo

    def mensagem(self, msg):
        print(msg)