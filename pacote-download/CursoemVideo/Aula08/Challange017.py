#Challange017 - Hipotenusa do triangulo retangulo
'''from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = hypot(co, ca)
print(f'A hipotenusa vai medir {h}')'''
#forma das cavernas
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = (ca**2 + co**2) ** (1/2)
print(f'A hipotenusa vai medir {h}')