d = int(input('Qual a distância da sua viagem: '))
print(f'Você está prestes a começar uma viagem de {d:.1f} km.')
if d <= 200:
    preço = d * 0.50
    print(f'E o preço da sua passagem será de R${preço:.2f}')
else:
    preço = d * 0.45
    print(f'E o preço da sua passagem será de R${preço:.2f}')
