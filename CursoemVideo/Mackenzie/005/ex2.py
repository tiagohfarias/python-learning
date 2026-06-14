soma = 500.0
while True:
    op = int(input())
    if op == 1:
        print(f'{soma:.2f}')
    elif op == 2:
        resgate = float(input())
        if resgate <= soma:
            print(f'{soma - resgate:.2f}')
            soma = soma - resgate
        elif resgate > soma:
            print(f'{soma:.2f}')
    elif op == 3:
        adicionar = float(input())
        print(f'{soma + adicionar:.2f}')
        soma = soma + adicionar
    elif op == 4:
        break
