from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
computer = randint(0,5) #Faz o computador "PENSAR" em um número
print('Em que número pensei?')
user = int(input('Digite sua resposta aqui: ')) #Usuario tenta adivinhar o número do computador
print('PROCESSANDO...')
sleep(3)
if user != computer:
    print(f'GANHEI! Eu pensei no número {computer} e não no {user}!')
else:
    print(f'PARABÉNS! Você conseguiu me vencer!')





