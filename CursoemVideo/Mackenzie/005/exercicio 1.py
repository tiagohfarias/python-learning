'''Uma lanchonete deseja um programa para registrar os itens consumidos por um cliente e calcular o valor total da conta.
O programa deve receber o nome de N itens consumidos (onde N representa uma quantidade variável de itens).
 A entrada de dados deve continuar até que o usuário digite a palavra fim como nome do item, indicando que não há mais produtos a registrar.
Para cada item informado (exceto quando o nome digitado for fim), o programa também deve receber:
1 - A quantidade consumida do item.
2- O preço unitário do item.
Para cada item registrado, o programa deve calcular e exibir o valor total daquele item (quantidade × preço unitário).
Ao final do registro de todos os itens, o programa deve exibir também o valor total da conta, considerando todos os itens consumidos.
O problema exige o uso de estrutura de repetição, pois o número de itens consumidos é variável e a entrada de dados termina somente quando o usuário digitar fim.'''
soma = 0
while True:
    n = input()
    if n == 'fim':
        break
    qtd = int(input())
    preco = float(input())
    valor = qtd * preco
    print(f'{valor:.2f}')
    soma += valor
print(f'{soma:.2f}')


