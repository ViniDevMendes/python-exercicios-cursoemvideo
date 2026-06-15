# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

antigo_salario = float(input('Digite o seu salário mensal: ')) # Salário sem os 15% de aumento
novo_salario = antigo_salario + (antigo_salario * 15 / 100)
print('O seu novo salário com o aumento de 15% é {:.2f}'.format(novo_salario))