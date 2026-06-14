def menu():
    print('(1) Cadastrar amigo (no final da lista)')
    print('(2) Cadastrar amigo (no início da lista)')
    print('(3)  Cadastrar amigo (em qualquer posição da lista)')
    print('(4) Remover um nome')
    print('(5) Mostrar os nomes de todos os amigos')
    print('(6) Substituir um nome')
    print('(7) Mostrar o número total de cadastros')
    print('(8) Colocar os nomes em ordem alfabética')
    print('(9) Sair do programa')
    op = int (input('Opção selecionada: '))
    while op <1 or op>9:
        op = int (input('Opção selecionada: '))
    return op

def inserir_amigo(amigo):
    nome = input('Nome: ')
    amigo.append(nome)

def inserir_inicio(amigo):
    nome = input('Nome: ')
    amigo.insert(0,nome)

def inserir_qualquer_posicao(amigo):
    posicao = int(input('Em qual posição você quer inseir?: '))
    nome = input('Nome: ')
    amigo.insert(posicao,nome)

def remover_amigo(amigo,pos=None):
    nome = input('Nome a ser removido: ')
    for i in range(0,len(amigo)):
        if amigo[i] == nome:
            pos = i
            break
        del amigo[pos]

def mostrar_nomes(amigo):
    print(amigo)

def substituir_nome(amigo):
    nome = input('Nome a ser substituido: ')
    nomenovo = input('Nome novo: ')
    for i in range(0, len(amigo)):
        if amigo[i] == nome:
            amigo[i] = nomenovo
            break

def total_cadastros(amigo):
    print('Total de amigos = %d' % len(amigo))

def ordenar_amigos(amigo):
    amigo.sort()
    mostrar_nomes(amigo)

def main():
    amigo = []
    while True:
        op = menu()
        if op == 9:
            break
        if op == 1:
            inserir_amigo(amigo)
        elif op == 2:
            inserir_inicio(amigo)
        elif op == 3:
            inserir_qualquer_posicao(amigo)
        elif op == 4:
            remover_amigo(amigo)
        elif op == 5:
            mostrar_nomes(amigo)
        elif op == 6:
            substituir_nome(amigo)
        elif op == 7:
            total_cadastros(amigo)
        elif op == 8:
            ordenar_amigos(amigo)

main()
