while True:
    print('\nSoma .................... +'
          '\nSubtração ............. -'
          '\nMultiplicação......... *'
          '\nDivisão................... /'
          '\nSair ....................... 0 ')
    op = input('Escolha uma das operações a partir dos respectivos símbolos: ')
    if op == '0':
        print('Saindo do programa...')
        break
    else:
        print('Digite dois números:')
        n1 = float(input())
        n2 = float(input())
    if op == '+':
        print(f'O resultado é igual a {n1 + n2}')
    elif op == '-':
        print(f'O resultado é igual a {n1 - n2}')
    elif op == '*':
        print(f'O resultado é igual a {n1 * n2}')
    elif op == '/':
        if n2 != 0:
            print(f'O resultado é igual a {n1 / n2}')
        else:
            print('Não há divisão por zero...')
    else:
        print('Opção invalida!')
