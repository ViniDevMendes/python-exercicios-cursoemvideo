# Leia duas notas de um aluno.
# Calcule a média.
#
# Média abaixo de 5.0:
# Reprovado
#
# Média entre 5.0 e 6.9:
# Recuperação
#
# Média 7.0 ou superior:
# Aprovado

"""

Lógica do enunciado:

1- pedir duas notas para o aluno
2- calcular a média entre elas
3- se a média for abaixo de 5, está reprovado
4- se a média esta entre 5.0 e 6.9, está em recuperação
5- se a média é 7 ou superior, está aprovado

"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
if media < 5:
    print(f"Você está reprovado, sua nota foi: {media:.2f}.")
elif media >= 5 and media < 7:
    print(f"Você está de recuperação, sua nota foi: {media:.2f}.")
else:
    print(f"Você está aprovado, sua nota foi {media:.2f}.")