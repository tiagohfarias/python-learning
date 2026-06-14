n = str(input('Digite seu nome completo: '))
name = n.split()
print(f'O seu primeiro nome é {name[0]}\n'
      f'O seu último nome é {name[len(name)-1]}')
#print(f'O seu último nome é {name[-1]}')
'''vi agora no gemini que ao invés de len(name)-1, posso colocar diretamente
{name[-1]}, ainda não tenho a explicação, mas o gemini disse que o Guanabara fala dps'''
