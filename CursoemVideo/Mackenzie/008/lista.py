lista = []
def quantidade():
    x = int(input('Quantidade de números na lista: '))
    return x

def entrada(x):
    for i in range(x):
        num = int(input('Digite o(s) número(s) pertencente a lista: '))
        lista.append(num)

def saida():
    for i in range (len(lista)):
        print('Valor: ', lista[i])

def main():
    x = quantidade()
    entrada(x)
    saida()
main()