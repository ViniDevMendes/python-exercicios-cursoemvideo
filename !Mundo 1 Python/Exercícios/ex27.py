# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome = str(input('Digite aqui o seu nome completo: ')).strip()
nome1 = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome1[0]))
print('Seu ultimo nome é: {}'.format(nome1[len(nome1)-1])) # o "len(nome1)" sabe quantas posiçãoes tem "nome"