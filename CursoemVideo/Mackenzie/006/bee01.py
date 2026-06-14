n = -1
while n <= 0:
    n = int(input())
    if n <= 0:
        n = int(input())
frios = 0
quentes = 0
soma = 0
for i in range(n):
    temp = float(input())
    if temp < 20:
        frios += 1
    else:
        quentes += 1
    maior_temp = temp
    if temp > maior_temp:
        maior_temp = temp
    soma += temp
    média = soma/n
print(frios)
print(quentes)
print(média)
print(maior_temp)