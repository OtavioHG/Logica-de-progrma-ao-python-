def calcular_imposto(valor_produto, taxa_imposto):
    
    valor_produto = float(valor_produto.replace(',', '.'))
    taxa_imposto = float(taxa_imposto.replace(',', '.'))

    
    imposto = valor_produto * (taxa_imposto / 100)

    
    return valor_produto + imposto



taxa_imposto = input("Digite a taxa de imposto em %: ")
valor_produto = input("Digite o valor do produto: ")

total_com_imposto = calcular_imposto(valor_produto, taxa_imposto)


print(f"O total com imposto é: R$ {total_com_imposto:.2f}")

