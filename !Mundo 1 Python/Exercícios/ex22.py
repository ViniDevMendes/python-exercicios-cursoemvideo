# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1 - O nome com todas as letras maíusculas 
# 2 - O nome com todas as letras minúsculas 
# 3 - Quantas letras tem ao todo (sem contar os espaços) 
# 4 - Quantas letras tem o primeiro nome 

nome = str(input('Qual o seu nome completo?: '))
print('Seu nome em maísculo fica {}'.format(nome.upper()))
print('Seu nome em minúsculo fica {}'.format(nome.lower()))
print('Seu nome tem um total de {} letras.'.format(len(nome) - nome.count(' '))) 
# nome.count(' '):  conta quantos espaços em branco existem dentro da string 'nome'
# len(nome) - nome.count(' '): calcula quantos caracteres restam na string 'nome' após subtrair todos os espaços em branco
# print('Seu primeiro nome tem um total de {} letras.'.format(nome.find(' ')))

# Separar os nomes como se fosse lista
separa = nome.split()
# nome.split(): Divide a string nome em partes separadas por espaços em branco e cria uma lista com essas partes
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
# separa[0]: Acessa o primeiro elemento da lista separa, que corresponde ao primeiro nome da string nome
# len(separa[0]): É usada para contar quantas letras existem no primeiro nome armazenado na variável separa[0]
