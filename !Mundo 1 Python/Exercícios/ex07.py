# Desenvolva um programa que leia as duas notas de um aluno, e calcule e mostre a sua média
#              JEITO DO VIDEO

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2) / 2 # o n1 + n2 está em () pq deve ser feita essa conta primeiro, pra depois dividir por 2
print('A média entre {:.2f} e {:.2f}, é igual a {:.2f}'.format(n1, n2, media))

#          JEITO QUE EU FIZ
# nota1 = float(input('Digita a primeira nota: '))
# nota2 = float(input('Digite a outra nota: '))
# media = (nota1 + nota2) / 2 # primeiro fazer a soma das notas, usando () para priorizar
# print('A média das notas do aluno é: {:.1f}!'.format(media))
