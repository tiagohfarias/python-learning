'''soma, sub , multi, div, div trunc, resto, exp'''
n1 = int(input())
n2 = int(input())
soma = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
div_trunc = n1 // n2
resto = n1 % n2
exponente = n1 ** n2
print(f'A soma é {soma}\nA sub é {sub}\nA multiplicacao é {mul}\nA div é {div}\nA div trunc é {div_trunc}'
      f'\nO resto é {resto}\nE a exponenciacaio é {exponente}')

"""Quadrado diferenca"""
n3 = int(input('Escreva um numero'))
n4 = int(input('escreva outro numero'))
qua_diff = n3**2 - 2*n3*n4 + n4**2
print(qua_diff)

'''concurseiro porcentagem do premio'''
premio = 780000
p1 = premio*0.46
p2 = premio*0.32
p3 = premio - p1 - p2
print(f'{premio}\n{p1}\n{p2}\n{p3}')