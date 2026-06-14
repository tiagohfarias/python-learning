print('Digite um conjunto de números(o número 0 encerra a entrada de dados)')
num = int(input())
maior = num
menor = num
soma = 0
while num != 0:
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    num = int(input())
print(f'Soma = {soma}\nMaior = {maior}\nMenor = {menor} ')