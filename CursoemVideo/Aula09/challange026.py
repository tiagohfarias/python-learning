name = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {name.count('A')} vezes na frase\n'
      f'A primeira letra A aparece na posição {name.find("A")+1}\n'
      f'A última letra A aparece na posição {name.rfind("A")+1}')

