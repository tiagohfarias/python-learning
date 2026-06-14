n1 = float(input())
n2 = float(input())
n3 = float(input())
media = (n1 + n2 + n3) / 3
print(f'{media:.1f}')
if media >=0 and media <3:
    print('Reprovado')
elif media <7:
    print('Exame')
    print('Você precisa tirar nota ')