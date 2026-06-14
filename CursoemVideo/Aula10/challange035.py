print('-='*30)
print('Analisador de Triângulos')
print('-='*30)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a+b>c and a+c > b and b+c > a:
    print('Os segmentos acima \033[1;33mPODEM\033[m formar um triângulo!')
else:
    print('Os segmentos acima \033[1;31mNÃO PODEM\033[m formar um triângulo!')