import os

restaurantes = [{'nome':'Sushizao', 'categoria':'japonesa', 'ativo': False},
                {'nome':'Pizza Suprema', 'categoria':'italiana', 'ativo': True},
                {'nome':'Cantina', 'categoria':'italiana', 'ativo': False}
                ]

# Site para estilizar textos no terminal https://fsymbols.com/

def alternar_estado_restaurante():
     """
     Altera o estado de um restaurante (ativo/inativo).
    """
     exibir_subtitulo('Alternando estado do restaurante')
     nome_restaurante = input('Digite o nome do restaurante que deseja alterar estado: ')
     restaurante_encontrado = False

     for restaurante in restaurantes:
          if nome_restaurante == restaurante['nome']:
               restaurante_encontrado = True
               restaurante['ativo'] = not restaurante['ativo']
               mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
               print(mensagem)
     if not restaurante_encontrado:
          print(f'O restaurante não foi encontrado')
     voltar_ao_menu_principal()
     
def exibir_nome_do_programa():
      '''
      exibe o nome do programa de forma estilizada
      '''
      print('''
      丂闩⻏ㄖ尺 🝗〤尸尺🝗丂丂      
      ''') 
def exibir_opcoes():
      '''
      exibe as opções para o usuário
      '''
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Alterar ativação do restaurante')
      print('4. Sair')

def finalizar_app():
    '''
    Finaliza o programa
    '''
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
     '''
     Retorna ao menu principal
     '''
     input('Digite qualquer tecla para voltar ao menu: ')
     main()

def opcao_invalida():
     '''
     informa que a opção selecionada é invalida e retorna ao menu
     '''
     print('Opção inválida\n')
     voltar_ao_menu_principal()

def exibir_subtitulo(texto):
     ''' 
     LImpa a tela e exibe o titulo escolhido separado por *
     '''
     os.system('cls')
     linha = '*' * (len(texto) + 4)
     print(linha)
     print(texto)
     print(linha)
     print()

def cadastrar_novo_restaurante():
     '''
     cadastra novos restaurantes dentro do dicionário restaurantes
     
     inputs: nome do restaurante, categoria
     '''
     exibir_subtitulo('Cadastro de novos restaurantes')
     nome_do_restaurante = input('Digite o nome do restaurante: ')
     categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
     dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
     print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
     restaurantes.append(dados_do_restaurante)
     voltar_ao_menu_principal()

def listar_restaurantes():
     '''
     Exibe a lista dos restaurantes cadastradas e suas informações
     '''
     exibir_subtitulo('Listando os restaurantes')

     print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
     
     for restaurante in restaurantes:
           
          nome_restaurante = restaurante['nome']
          categoria = restaurante['categoria']
          ativacao = 'ativado' if restaurante['ativo'] else 'desativado'
          print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativacao}')

     voltar_ao_menu_principal()

def escolher_opcao ():
      '''
      direciona o programa para opção escolhida pelo usuário
      '''
      try:
            opcao_escolhida = int(input("Escolha uma opção: "))
            print (f'você escolheu a opção: {opcao_escolhida}')

            if opcao_escolhida == 1:
                  cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                  listar_restaurantes()
            elif opcao_escolhida == 3:
                  alternar_estado_restaurante()
            elif opcao_escolhida == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      except:
           opcao_invalida()

def main():
    '''
    Inicia o programa
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

'''
verifica se o módulo atual está sendo executado como o programa principal
'''
if __name__ == '__main__':
    main()