''''Faça um programa em Python que solicite ao usuário a quantidade de números inteiros aleatórios
entre 1 e 10 que ele deseja que este programa gere. Após gerar e apresentar esses números randômicos,
o programa deve mostrar a soma destes valores.'''

from random import randint
qtd = int(input('Digite a quantidade de números inteiros que serão gerados, escolha entre 1 a 10 números: '))
soma = 0
print('\nNúmeros gerados:')
for i in range(qtd):
    aleatorio = randint(1, 10)
    print(aleatorio)
    soma += aleatorio
print('-' * 20)
print(f'A soma final foi {soma}')
