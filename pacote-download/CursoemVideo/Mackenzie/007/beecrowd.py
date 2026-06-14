def eh_triangulo(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("Os lados formam um triângulo")
        return True
    else:
        print("Os lados não formam um triângulo")
        return False

def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    lado1 = int(input())
    lado2 = int(input())
    lado3 = int(input())

    if eh_triangulo(lado1, lado2, lado3):
        tipo = tipo_triangulo(lado1, lado2, lado3)
        print(tipo)

main()