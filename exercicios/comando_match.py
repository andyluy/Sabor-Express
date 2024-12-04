opcao_escolhida = int(input('Escolha uma opção: '))
match opcao_escolhida:
    case 1:
        print('Adicionar restaurante')
    case 2:
        print('Listar restaurantes')
    case 3:
        print('Ativar restaurante')
    case 4:
        print('Finalizar app')
    case _:
        print('Opção inválida!')

# # Estrutura básica:
# match expressão:
#     case padrão_1:
#         # Código a ser executado se expressão corresponder a padrão_1
#     case padrão_2:
#         # Código a ser executado se expressão corresponder a padrão_2
#     # ... outros casos ...
#     case _:
 # # Código a ser executado se nenhum dos padrões anteriores corresponder. Isso é útil para tratar casos não específicos.