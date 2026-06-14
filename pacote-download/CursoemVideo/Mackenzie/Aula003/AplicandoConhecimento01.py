'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos),
deve pagar uma multa de R$ 4.00 por quilo excedente, porém toda vez que ele cumpre o estabelecido pelo regulamento de pesca do
estado de São Paulo, ele recebe uma bonificação de R$ 1.00 por quilo pescado.
    João precisa que você faça um programa, em Python, que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Apresente, na saída de dados, a quantidade de quilos em excesso e o valor da multa, com 2 casas decimais,
quando ele infringe o regulamento.
Caso ele atenda o regulamento, apresente, na saída de dados, o valor total da bonificação, com 2 casas decimais).'''
'''peso = float(input('Quantos kilos de peixe você pescou hoje? '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print (f'Você excedeu o limite de peso em: {excesso} kg.')
    print (f'Por isso terá que pagar uma multa de R$ {multa:.2f}')
else:
    bonificacao = peso
    print(f'Você está na norma de peso de peixe do estado de SP , por isso recebeu uma bonificação de R$ {bonificacao:.2f}')'''

peso = float(input())
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'{excesso:.2f}')
    print(f'{multa:.2f}')
else:
    bonificacao = peso
    print(f'{bonificacao:.2f}')
