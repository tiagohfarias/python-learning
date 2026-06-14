s = 0
num = 1
for d in range(1,51):
    denominador = d
    s += num/d
    if d !=50:
        print(f'{num}/{d} + ', end = '')
    else:
        print(f'{num}/{d} = ', end = '')
    num += 2
print(s)
