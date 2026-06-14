#First try with IF
vel = float(input('What is velocity that you drive?'))
if (vel>50):
    print('You will be fined')
print('End')

#Par ou impar
n1 = float(input('Enter a number: '))
if n1%2==0:
    print(f'The number {n1:.0f} is even')
else:
    print(f'The number {n1:.0f} is odd')

#quadrado do maior
import math
n1= float(input('Enter a number: '))
n2 = float(input('Enter other number: '))
if n1>n2:
    quadrado = math.pow(n1,2)
else:
    quadrado = math.pow(n2,2)
print(f'O quadrado do maior é {quadrado:.1f}')


