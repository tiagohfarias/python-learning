codigo = input('Digite o código de barras: ')

primeiros12 = codigo[:12]
ultimodigito = int(codigo[12])

soma = 0

for i in range(12):
    numero = int(primeiros12[i])
    if i % 2 == 0:
        soma += numero * 1
    else:
        soma += numero * 3

resto = soma % 10
if resto == 0:
    verificador = 0
else:
    verificador = 10 - resto

if verificador == ultimodigito:
    print('\033[32mCÓDIGO VÁLIDO!!\033[m')
else:
    print('\033[31mCÓDIGO INVÁLIDO!!\033[m')