a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
#Verificando quem é menor
menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é maior
maior = b
if a>b and a>c:
    maior = a
if c>a and c>b:
    maior = c
print(f'O MENOR número digitado foi {menor}\n'
      f'e o MAIOR foi {maior}\n')