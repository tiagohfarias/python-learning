vel = int(input('Qual é a velocidade do carro? '))
multa = (vel-80)*7
if vel <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h\n'
          f'Você deve pagar uma multa de {multa:.2f}R$!\n'
          f'Tenha um bom dia! Dirija com segurança!')