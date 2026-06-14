def adicionar_participacao(modalidades, participantes):
    for i in range(5):
        nome = input("")
        qtd = int(input(""))
        modalidades.append(nome)
        participantes.append(qtd)


def modalidade_mais_participantes(modalidades, participantes):
    maior_qtd = max(participantes)
    indice_maior = participantes.index(maior_qtd)
    nome_maior = modalidades[indice_maior]
    return nome_maior, maior_qtd


def modalidade_menos_participantes(modalidades, participantes):
    menor_qtd = min(participantes)
    indice_menor = participantes.index(menor_qtd)
    nome_menor = modalidades[indice_menor]
    return nome_menor, menor_qtd


def main():
    modalidades = []
    participantes = []

    adicionar_participacao(modalidades, participantes)

    nome_maior, qtd_maior = modalidade_mais_participantes(modalidades, participantes)
    nome_menor, qtd_menor = modalidade_menos_participantes(modalidades, participantes)

    print(f"{nome_maior} - {qtd_maior}")
    print(f"{nome_menor} - {qtd_menor}")


if __name__ == "__main__":
    main()