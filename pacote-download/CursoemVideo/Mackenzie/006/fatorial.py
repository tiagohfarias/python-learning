fat = 1
num = int(input('Digite um número inteiro e natural: '))
while num < 0:
    print('ERRO...Digite um número que seja natural, ou seja, > 0')
    num = int(input('Digite um número inteiro e natural: '))
for i in range(1, num + 1):
    fat *= i
print(f'{"-"*20}\nO resultado do fatorial é {fat}')