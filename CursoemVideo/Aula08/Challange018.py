#Challange018 - Sen, Cos, Tan
from math import sin,cos,tan,radians
ang = float(input('Digite um ângulo qualquer e descubra seu valor em sen(x),cos(x) e tg(x): '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'O ângulo de {ang} tem o Seno de {sen:.2f}')
print(f'O ângulo de {ang} tem o Cosseno de {cos:.2f}')
print(f'O ângulo de {ang} tem a Tangente de {tan:.2f}')