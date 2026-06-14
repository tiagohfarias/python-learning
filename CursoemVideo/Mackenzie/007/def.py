#Função para atualizar o preço com 10% de aumento
def atualiza_preco(valor):
    novo_valor = valor * 1.10
    return novo_valor


#Função para calcular a taxa de 2.5%
def taxa(valor_atualizado):
    valor_taxa = valor_atualizado * 0.025  # Calcula a taxa sobre o novo preço
    return valor_taxa  # Retorna o valor da taxa [cite: 133]

#Programa Principal
def main():
    preco_inicial = float(input("Digite o valor do produto: "))

    preco_final = atualiza_preco(preco_inicial)
    valor_da_taxa = taxa(preco_final)

    print(f"Valor atualizado: R$ {preco_final:.2f}")
    print(f"Valor da taxa: R$ {valor_da_taxa:.2f}")

main()