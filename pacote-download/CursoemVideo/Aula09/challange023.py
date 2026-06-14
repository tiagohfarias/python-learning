n1 = int(input('Write a number: '))
print(f'Analysing your number: {n1}')
o = n1 // 1 % 10
te = n1 // 10 % 10
hun = n1 // 100 % 10
th = n1 // 1000 % 10
print(f'Ones: {o}')
print(f'Tens: {te}')
print(f'Hundreds: {hun}')
print(f'Thousands: {th}')