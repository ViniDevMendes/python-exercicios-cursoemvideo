# Leia o preço de um produto.
#
# Mostre opções de pagamento:
# 1 - Dinheiro/Pix
# 2 - Cartão à vista
# 3 - Cartão 2x
# 4 - Cartão 3x ou mais
#
# Calcule o valor final de acordo com a opção escolhida.

"""

Lógica do enunciado:

1- Perguntar o preço de um produto
2- mostrar as opções de pagamento
3- calcular valor final conforme condição escolhida

"""

valor_item = float(input("Digite o valor do item desejado: R$ "))

condicao_pagamento = int(input("[1] para pagamento no Dinheiro/Pix\n[2] para pagamento no Cartão de Crédito a vista\n[3] para pagamento parcelado em 2x no Cartão de crédito\n[4] para pagamento parcelado em mais de 3x no Cartão de Crédito\nR: "))
if condicao_pagamento == 1:
    print(f"A opção escolhida foi no Pix/Dinheiro!\nO valor total para pagamento seria de R$ {valor_item} reais.")
elif condicao_pagamento == 2:
    print(f"A opção escolhida foi no Cartão de Crédito à vista!\nO valor total para pagamento seria de R$ {valor_item} reais.")
elif condicao_pagamento == 3:
    valor_parcelado = valor_item / 2
    print(f"A opção escolhida foi no Cartão de Crédito parcelado em 2x!\nO valor de cada parcela será de R$ {valor_parcelado} reais.")
elif condicao_pagamento == 4:
    qtd_parcelas = int(input("Você pode parcelar a compra de 3x a 12x, quantas parcelas deseja realizar? "))
    valor_parcelado = valor_item / qtd_parcelas
    print(f"A opção escolhida foi no Cartão de Crédito parcelado em até 12x!\nConsiderando ser em {qtd_parcelas} parcelas, o valor de cada seria de R$ {valor_parcelado} reais!")
else:
    print("Opção errada, tente novamente.")