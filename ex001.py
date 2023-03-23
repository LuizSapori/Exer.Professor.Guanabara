from colorama import init, Fore , Back , Style
init(autoreset=True)

# 1 - Variáveia
#MEIA = 'MEIA'
#INTEIRA = 'INTEIRA'
COMPRAR = 1
VER_ASSENTOS = 2
RESUMO_VENDAS = 3
SAIR = 4
JANELA = 'J'
CORREDOR = 'C'
DIREITA = 'D'
ESQUERDA = 'E'
ASSENTO_VAZIO = ''
PASSAGENS_DISPONIVEIS = 28
ASSENTOS_COLUNA = PASSAGENS_DISPONIVEIS // 4
#VALOR_PASSAGEM = 100
VENDA = 0
# 2 - Cabeçalho

print()
print( Fore.BLUE + Back.BLACK + '     PPROJETO POCCOBUS     ')
print()


# 3 - Menu

def menu_passagem():
    print('*-------------------------------------*')
    print('  |    MENU - VENDA DE PASSAGENS    | ')
    print('*-------------------------------------*')
    print('[ 1 ] Comprar passagem')
    print('[ 2 ] Assentos disponíveis')
    print('[ 3 ] Resumo Vendas')
    print('[ 4 ] Sair')
    print('*-------------------------------------*')
    return int(input('Selecione uma opção:  '))

def assentos_vendidos(assentos):
    return True if assentos == 'X' else False

def todos_assentos_vendidos(assentos):
    return ASSENTO_VAZIO not in assentos

def busca_posicoes_livres(assentos):
    posicoes_livres = []
    for indice, assentos in enumerate(assentos, start=1):
        if not assentos_vendidos(assentos):
            posicoes_livres.append(indice)
    return posicoes_livres

def assentos_livres(assentos_livres):
    posicoes_livres = ' - '.join(str(numero_poltrona) for numero_poltrona in assentos_livres)
    print(posicoes_livres)


def comprar_passagem(janela_direita,  corredor_direita, janela_esquerda, corredor_esquerda, total_vendido):
    while total_vendido <= PASSAGENS_DISPONIVEIS:
        print(Fore.BLUE+ 'VENDA DE PASSAGENS')
        print()

        #idade = obter_idade()
        #paga_meia = idade < 5 or idade > 65
        #if paga_meia:
        #    quantidade_vendidos[MEIA] += 1
        #else:
        #    quantidade_vendidos[INTEIRA] += 1

        print(Fore.BLUE+ 'ESCOLHA SEU ASSENTO: ')
        print()
        assentos_disponiveis()

        janela_ou_corredor = input('Digite opção Janela [ J ] ou Corredor [ C ]?: ').upper()
        if janela_ou_corredor == JANELA:
            direira_ou_esquerda = input('Janela direita [ D ] ou esquerda [ E ]: ').upper()
            if direira_ou_esquerda == DIREITA:
                vender_uma_passagem(janela_direita, total_vendido)
            elif direira_ou_esquerda == ESQUERDA:
                vender_uma_passagem(janela_esquerda, total_vendido)
            else:
                print('Opção inválida!')

        elif janela_ou_corredor == CORREDOR:

            opcao_direira_ou_esquerda = input('Corredor direita [ D ] ou esquerda [ E ]: ').upper()
            if opcao_direira_ou_esquerda == DIREITA:
                vender_uma_passagem(corredor_direita, total_vendido)
            elif opcao_direira_ou_esquerda == ESQUERDA:
                vender_uma_passagem(corredor_esquerda, total_vendido)
            else:
                print('Opção inválida!')

        else:
            print('Opção inválida!')

        if total_vendido == 28:
            print('\n***** Todas as passagens foram vendidas! *****\n')
            break

        comprar_mais = input('Deseja comprar outra passagem? [S/N]: ').upper()
        if comprar_mais == 'S':
            continue
        else:
            break


#def obter_idade():
#    idade_valida = False
#    idade = 0
#    while not idade_valida:
#        idade = int(input('Qual a idade do passageiro?: '))
#        if 0 <= idade <= 120:
#            idade_valida = True
#        else:
#            print('Idade inválida, digite novamente!')
#    return idade


def vender_uma_passagem(poltronas, total_passagens):
    if todos_assentos_vendidos(poltronas):
        print('Todos os lugares estão ocupados!')

    print('Posições livres:')
    lista_posicoes_livres = busca_posicoes_livres(poltronas)
    assentos_livres(lista_posicoes_livres)

    finalizou_compra = False
    while not finalizou_compra:
        polcompra = int(input('\nDigite o número da poltrona desejada: '))
        if polcompra in lista_posicoes_livres:
            poltronas[polcompra - 1] = 'X'
            total_passagens += 1
            finalizou_compra = True
        else:
            print('Opção invalida! Escolha uma poltrona válida!')
            finalizou_compra = False

    print('\n Operação efetuada com sucesso!! \n')


def assentos_disponiveis():
    print(Fore.GREEN+'   Lugares vagos [ ]' + Fore.RED+ '   Lugares ocupados [X]\n')
    print('     1  2  3  4  5  6  7')

    print('    ', end='')
    for poltronas in janela_direita:
        print(f'[{(poltronas if poltronas else " ")}]', end='')
    print('   -> Janela Direita')

    print('    ', end='')
    for poltronas in corredor_direita:
        print(f'[{(poltronas if poltronas else " ")}]', end='')
    print('   -> Corredor Direito')

    print('    ', end='')
    for poltrona in corredor_esquerda:
        print(f'[{poltrona if poltrona else " "}]', end='')
    print('   -> Corredor Esquerdo')

    print('    ', end='')
    for poltrona in janela_esquerda:
        print(f'[{(poltrona if poltrona else " ")}]', end='')
    print('   -> Janela Esquerda')

    print('    ', end='')

def resumo_vendas():
#    valor_meia = (quantidade_vendidos[MEIA] * VALOR_PASSAGEM) / 2
#    valor_inteira = quantidade_vendidos[INTEIRA] * VALOR_PASSAGEM
#    valor_total = valor_meia + valor_inteira

#    if total_vendido >= NUMERO_PASSAGENS_DISPONIVEIS / 2:
#        print('O numero minimo de passagens foi atingido! A viagem foi confirmada.')
#    else:
#        print('O numero minimo de passagens não foi atingido. A viagem esta cancelada!')

    print(f'O NÚMERO DE PASSAGENS VENDIDAS FORAM {VENDA} restam {PASSAGENS_DISPONIVEIS - VENDA} PASSAGENS!')


if __name__ == '__main__':
    # Declaração de Variáveis
    janela_direita = [ASSENTO_VAZIO] * ASSENTOS_COLUNA
    corredor_direita = [ASSENTO_VAZIO] * ASSENTOS_COLUNA
    janela_esquerda = [ASSENTO_VAZIO] * ASSENTOS_COLUNA
    corredor_esquerda = [ASSENTO_VAZIO] * ASSENTOS_COLUNA
#    quantidade_vendidos = {MEIA: 0, INTEIRA: 0}
    total_vendido = 0

    while True:
        opcao_menu = menu_passagem()

        if opcao_menu == COMPRAR:
            VENDA = 0
            VENDA = VENDA + 1
            comprar_passagem(janela_direita,corredor_direita,janela_esquerda,corredor_esquerda,total_vendido)

        elif opcao_menu == VER_ASSENTOS:
            print('Ver assentos\n')
            assentos_disponiveis()

        elif opcao_menu == RESUMO_VENDAS:
            assentos_disponiveis()
            resumo_vendas()
            break

        elif opcao_menu == SAIR:
            break


