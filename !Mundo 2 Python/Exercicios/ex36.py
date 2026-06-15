# Um banco analisa empréstimos.
# Leia o valor da casa, salário do comprador e anos de financiamento.
# A prestação mensal não pode ultrapassar 30% do salário.
# Informe se o empréstimo foi aprovado ou negado.

"""

Lógica do enunciado:

1- perguntar o valor da casa que deseja comprar / ok
2- perguntar o salario mensal liquido do possível comprador / ok
3- perguntar em quantos anos deseja financiar (ou meses?) / ok
3- verificar quanto seria 30% do salario do possível comprador / ok
5- o valor mensal da parcela não pode passar de 30% do salario /
6- após, informar se o financiamento foi aprovado ou não /


"""

import os

valor_casa = float(input("Digite o valor da casa que deseja comprar: "))
salario_mensal = float(input("Digite o seu salário liquido mensal: "))
anos_financiamento = int(input("Digite em quantos anos deseja financiar a casa: "))

meses_financiamento = anos_financiamento * 12  # calcula a quantidade de meses, conforme quantos anos foram escolhidos

limite_30_porcento = salario_mensal * 0.3  # calcula qual seria os 30% do salario digitado
valor_parcela_mensal = valor_casa / meses_financiamento  # valor que será pago por mes

os.system("cls")

if valor_parcela_mensal > limite_30_porcento:
    print(f"Financiamente negado, o valor ultrapassa 30% da sua renda mensal.\nO valor máximo da parcela seria de R$ {limite_30_porcento:.2f} reais.")
else:
    print(f"Financiamento aprovado!\nO valor da parcela mensal seria de R$ {valor_parcela_mensal:.2f} reais, e, irá pagar por {anos_financiamento} anos!")
