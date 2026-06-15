# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%
#         JEITO DO VÍDEO

salario = float(input('Qual é o salário do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))




# #      JEITO QUE EU FIZ
# salario = float(input('Digite o valor do seu salário atual: R$ '))
# if salario >= 1250:
#     aumento = salario * 0.10
#     print('Seu novo salário com um aumento de 10% será: {:.2f}'.format(salario + aumento))
# else:
#     aumento2 = salario * 0.15
#     print('Seu novo salário com um aumento de 15% será: {:.2f}'.format(salario + aumento2))
# print('Parabéns pelo aumento! :)')